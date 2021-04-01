class Solution {
    public int uniquePaths(int m, int n) {
        int[] arr = new int[n];
        Arrays.fill(arr, 1);
        for (int j = 1; j < m; ++j) {
            for (int i = 1; i < arr.length; ++i) {
                arr[i] = arr[i-1] + arr[i];
            }
        }
        
        return arr[n-1];
    }
}