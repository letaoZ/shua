class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (nums == null || nums.length == 0) return 0;
        int i = 0;
        int j = 0;
        int product = 1;
        int result = 0;
        while (j < nums.length) {
            product *= nums[j];
            while (i <= j) {
                if (product < k) break;
                else {
                    product /= nums[i];
                    i++;
                }
            }
            
            if (i <= j) {
                result += j - i + 1;
            } else {
                product = 1;
            }
            j++;
        }
        
        return result;
    }
}