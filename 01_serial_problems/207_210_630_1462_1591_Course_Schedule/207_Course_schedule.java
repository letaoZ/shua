class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] in = new int[numCourses];
        Queue<Integer> q = new LinkedList<>();
        ArrayList<Integer>[] adj = new ArrayList[numCourses];
        
        for (int[] p : prerequisites) {
            // w -> v
            int w = p[0];
            int v = p[1];
            in[v]++;
            if (adj[w] == null) adj[w] = new ArrayList<Integer>();
            adj[w].add(v);
        }
        
        for (int i = 0; i < numCourses; ++i) {
            if (in[i] == 0) q.add(i);
        }
        
        int count = 0;
        while (!q.isEmpty()) {
            int w = q.poll();
            count++;
            if (adj[w] != null && adj[w].size() != 0) {
                for (int v : adj[w]) {
                    if (--in[v] == 0) q.add(v);
                }
            }
        }
        
        if (count == numCourses) return true;
        return false;
    }
}