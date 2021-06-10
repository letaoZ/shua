class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0;
        int u = nums.length - 1;
        
        while (l < u) {
            int m = l + (u - l) / 2;          
            if (nums[m] > nums[m+1]) u = m;
            else l = m + 1;
        }
        
        return l;
    }
}