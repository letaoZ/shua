import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Stack;

public class TextEditor {
    private Map<String, DocNode> map;
    private HashSet<String> active;
    private String buf = "";
    private DocNode head;
    private DocNode tail;

    public TextEditor() {
        map = new HashMap<>();
        this.head = new DocNode(null);
        this.tail = new DocNode(null);
        this.head.next = tail;
        this.tail.prev = head;
        active = new HashSet<>();
    }

    public String open(String docName) {
        if (!map.containsKey(docName)) {
            Document view = new Document();
            DocNode node = new DocNode(view);
            insertNode(node);
            map.put(docName, node);
            active.add(docName);
            return view.getText();
        }

        DocNode node = map.get(docName);
        if (active.contains(docName)) {
            promoteNode(node);
        } else {
            insertNode(node);
            active.add(docName);
        }

        return node.doc.getText();
    }

    public String close(String docName) {
        if (!map.containsKey(docName)) return "";
        DocNode node = map.get(docName);
        if (!active.contains(docName)) return node.doc.getText();

        disconnectNode(node);
        active.remove(docName);
        node.doc.close();
        return node.doc.getText();
    }

    public String append(String str) {
        if (this.head.next == this.tail) return "";
        return this.head.next.doc.append(str);
    }

    public String move(int pos) {
        if (this.head.next == this.tail) return "";
        return this.head.next.doc.move(pos);
    }

    public String delete() {
        if (this.head.next == this.tail) return "";
        return this.head.next.doc.delete();
    }

    public String select(int l, int r) {
        if (this.head.next == this.tail) return "";
        return this.head.next.doc.select(l, r);
    }

    public String copy() {
        if (this.head.next == this.tail) return "";
        this.buf = this.head.next.doc.copy();
        return this.head.next.doc.getText();
    }

    public String paste() {
        if (this.head.next == this.tail) return "";
        this.head.next.doc.append(this.buf);
        return this.head.next.doc.getText();
    }

    public String undo() {
        if (this.head.next == this.tail) return "";
        return this.head.next.doc.undo();
    }

    public String redo() {
        if (this.head.next == this.tail) return "";
        return this.head.next.doc.redo();
    }

    private void disconnectNode(DocNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = null;
        node.next = null;
    }

    private void insertNode(DocNode node) {
        node.prev = this.head;
        node.next = this.head.next;
        this.head.next.prev = node;
        this.head.next = node;
    }

    private void promoteNode(DocNode node) {
        disconnectNode(node);
        insertNode(node);
    }

    public static void main(String[] args) {
        TextEditor t = new TextEditor();
        System.out.println(t.open("document1"));
        System.out.println(t.append("Hello, world!"));
        System.out.println(t.select(7, 12));
        System.out.println(t.copy());
        System.out.println(t.delete());
        System.out.println(t.open("document2"));
        System.out.println(t.paste());
        System.out.println(t.close("document2"));
        System.out.println(t.undo());
        System.out.println(t.open("document2"));
        System.out.println(t.undo());
    }
}

class DocNode {
    public Document doc;
    public DocNode prev;
    public DocNode next;

    public DocNode(Document doc) {
        this.doc = doc;
        this.prev = null;
        this.next = null;
    }
}

class Document {
    private String current = "";
    private String buf = "";

    private int l = 0;
    private int r = 0;

    private Stack<State> undoStack;
    private Stack<State> redoStack;

    public Document() {
        undoStack = new Stack<State>();
        redoStack = new Stack<State>();
    }

    public String getText() {
        return this.current;
    }

    public String close() {
        this.undoStack = new Stack<>();
        this.redoStack = new Stack<>();
        this.l = this.current.length();
        this.r = this.current.length();
        return this.current;
    }

    public String move(int offset) {
        if (offset < 0) this.l = 0;
        else if (offset > current.length()) this.l = current.length();
        else this.l = offset;
        this.r = this.l;
        return current;
    }

    public String append(String str) {
        undoStack.push(new State(current, l, r));
        redoStack = new Stack<>();
        String p1 = this.current.substring(0, l);
        String p2 = this.r < this.current.length() ? this.current.substring(r) : "";
        this.l += str.length();
        this.r = this.l;
        this.current = p1 + str + p2;
        return this.current;
    }

    public String delete() {
        undoStack.push(new State(current, l, r));
        redoStack = new Stack<>();
        if (this.r == this.l) {
            if (this.r < this.current.length()) {
                this.current = this.current.substring(0, l) + this.current.substring(l + 1);
            }
            return this.current;
        }

        if (this.r > this.current.length()) this.r = this.current.length();

        if (this.l < this.r) {
            this.current = this.current.substring(0, l) + this.current.substring(r);
            this.r = this.l;
        }

        return this.current;
    }

    public String select(int l, int r) {
        if (l < 0) this.l = 0;
        else this.l = Math.min(l, this.current.length());
        if (r < 0) this.r = 0;
        else this.r = Math.min(r, this.current.length());

        if (l > r) return select(r, l);

        return this.current;
    }

    public String copy() {
        return this.current.substring(this.l, this.r);
    }

    public String paste() {
        this.append(buf);
        return this.current;
    }

    public String undo() {
        if (!undoStack.isEmpty()) {
            State state = undoStack.pop();
            redoStack.push(new State(this.current, this.l, this.r));
            this.current = state.current;
            this.l = state.l;
            this.r = state.r;
        }

        return this.current;
    }

    public String redo() {
        if (!redoStack.isEmpty()) {
            undoStack.push(new State(this.current, this.l, this.r));
            State state = redoStack.pop();
            this.current = state.current;
            this.l = state.l;
            this.r = state.r;
        }

        return this.current;
    }
}

class State {
    public int l;
    public int r;
    public String current;

    public State(String current, int l, int r) {
        this.current = current;
        this.l = l;
        this.r = r;
    }
}
