class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int u = nums.length - 1;
        
        while (l < u) {
            int m = l + (u - l) / 2;
            
            if (nums[m] < nums[u]) u = m;
            else if (nums[m] > nums[u]) l = m + 1;
            else u--;
        }
        
        return nums[l];
    }
}