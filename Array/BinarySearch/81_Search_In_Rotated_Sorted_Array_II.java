class Solution {
    public boolean search(int[] nums, int target) {
        int l = 0;
        int u = nums.length - 1;
        
        while (l <= u) {
            int m = l + (u - l) / 2;
            
            if (nums[m] == target) return true;
            
            if (nums[m] < nums[u]) {
                if (target <= nums[u] && target > nums[m]) l = m + 1;
                else u = m - 1;
            } else if (nums[m] > nums[u]) {
                if (target < nums[m] && target > nums[u]) u = m - 1;
                else l = m + 1;
            } else {
                u--;
            }
        }
        
        return false;
    }

    // Lessons learn: Think of both rotated or not rotated situation. Only get rid of the half that are absolutely safe (without missing the target)
    public boolean searchEarlierAttemptWrongAnswer(int[] nums, int target) {
        int l = 0;
        int u = nums.length - 1;
        
        while (l <= u) {
            int m = l + (u - l) / 2;
            
            if (nums[m] == target) return true;
            
            if (nums[m] < nums[u]) {
                if (target > nums[u]) u = m - 1;
                else l = m + 1;
            } else if (nums[m] > nums[u]) {
                if (target < nums[m] && target > nums[u]) u = m - 1;
                else l = m + 1;
            } else {
                u--;
            }
        }
        
        return false;
    }
}