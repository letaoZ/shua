class Solution {
    public int arraySign(int[] nums) {
        int x = 0;
        int y = 1 << 31;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == 0) return 0;
            else x ^= (nums[i] & y);
        }
        
        return x == 0 ? 1 : -1;
    }
}