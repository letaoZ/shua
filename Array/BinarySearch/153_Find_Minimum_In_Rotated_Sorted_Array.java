class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int u = nums.length - 1;
        if (nums[u] > nums[l]) return nums[l];
        
        while (l < u) {
            int m = l + (u - l) / 2;
            
            if (nums[u] > nums[m]) u = m;
            else l = m + 1;
        }
        
        return nums[l];
    }

    public int findMinEarlierAttempt1(int[] nums) {
        int l = 0;
        int u = nums.length - 1;
        
        while (l + 1 < u) {
            int m = l + (u - l) / 2;
            
            if (nums[l] > nums[m] && nums[u] > nums[m]) u = m;
            else if (nums[l] < nums[m] && nums[u] < nums[m]) l = m;
            else return nums[l]; // this can be optimized
        }
        
        return Math.min(nums[l], nums[u]);
    }

    public int findMinEarlierAttempt2(int[] nums) {
        int l = 0;
        int u = nums.length - 1;
        if (nums[u] > nums[l]) return nums[l];
        
        while (l + 1 < u) {
            int m = l + (u - l) / 2;
            
            if (nums[l] > nums[m] && nums[u] > nums[m]) u = m;
            else l = m;
        }
        
        return Math.min(nums[l], nums[u]);
    }

    class Solution {
        public int findMinEarlierAttempt3(int[] nums) {
            int l = 0;
            int u = nums.length - 1;
            if (nums[u] > nums[l]) return nums[l];
            
            while (l + 1 < u) {
                int m = l + (u - l) / 2;
                
                if (nums[u] > nums[m]) u = m;
                else l = m;
            }
            
            return Math.min(nums[l], nums[u]);
        }
    }
}