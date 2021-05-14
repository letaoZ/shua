class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int i = 0;
        int sum = 0;
        int result = nums.length + 1;
        for (int j = 0; j < nums.length; ++j) {
            sum += nums[j];
            while (sum >= target && sum > 0) {
                result = Math.min(result, j - i + 1);
                sum -= nums[i++];
            }
        }
        
        return result == nums.length + 1 ? 0 : result;
    }
}