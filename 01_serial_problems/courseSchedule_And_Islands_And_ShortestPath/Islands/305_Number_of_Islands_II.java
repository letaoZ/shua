class Solution {
    private int[] rank;
    private int[] parent;
    private int count = 0;
    
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        initUnionFind(m * n);
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < positions.length; ++i) {
            int node = n * positions[i][0] + positions[i][1];
            if (parent[node] != -1) {
                result.add(count);
                continue;
            }
            addNode(node);
            
            int[] dx = new int[] {0, 0, 1, -1};
            int[] dy = new int[] {1, -1, 0, 0};
            
            for (int k = 0; k < 4; ++k) {
                int x = positions[i][0] + dx[k];
                int y = positions[i][1] + dy[k];
                
                if (x >= 0 && x < m && y >= 0 && y < n && parent[n * x + y] != -1) unite(n * x + y, n * positions[i][0] + positions[i][1]);
            }
            
            result.add(count);
        }
        
        return result;
    }
    
    public void initUnionFind(int size) {
        rank = new int[size];
        parent = new int[size];
        for (int i = 0; i < size; ++i) {
            rank[i] = 0;
            parent[i] = -1;
        }
    }
    
    public void addNode(int x) {
        parent[x] = x;
        count++;
    }
    
    public int find(int x) {
        if (parent[x] == -1) return -1;
        if (parent[x] == x) return x;
        else return parent[x] = find(parent[x]);
    }
    
    public void unite(int x, int y) {
        x = find(x);
        y = find(y);
        
        if (x == y) return;
        
        count--;
        if (rank[x] < rank[y]) {
            parent[x] = y;
        } else {
            parent[y] = x;
            if (rank[x] == rank[y]) rank[x]++;
        }
    }
}