class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int sum = 0;
        Map<Integer, Integer> smap = new HashMap<>();
        smap.put(0, -1);
        for (int i = 0; i < nums.length; ++i) {
            sum += nums[i];
            int x = sum % k;
            if (smap.containsKey(x)) {
                if (i - smap.get(x) >= 2) return true;
            } else {
                smap.put(x, i);
            }
        }
        
        return false;
    }
}