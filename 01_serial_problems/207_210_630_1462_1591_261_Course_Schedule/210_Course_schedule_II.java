class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] in = new int[numCourses];
        Queue<Integer> q = new LinkedList<>();
        ArrayList<Integer>[] adj = new ArrayList[numCourses];
        Stack<Integer> stack = new Stack<>();
        
        for (int[] e : prerequisites) {
            // w    -> v
            // ai   -> bi
            // e[0] -> e[1]
            
            int w = e[0];
            int v = e[1];
            in[v]++;
            if (adj[w] == null) adj[w] = new ArrayList<Integer>();
            adj[w].add(v);
        }
        
        for (int n = 0; n < numCourses; ++n) {
            if (in[n] == 0) q.add(n);
        }
        
        while (!q.isEmpty()) {
            int w = q.poll();
            stack.push(w);
            if (adj[w] != null) {
                for (int v : adj[w]) {
                    if (--in[v] == 0) q.add(v);
                }
            }
        }
        
        if (stack.size() != numCourses) return new int[0];
        int[] result = new int[numCourses];
        for (int i = 0; i < numCourses; ++i) result[i] = stack.pop();
        return result;
    }
}