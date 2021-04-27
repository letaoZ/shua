class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> smap = new HashMap<>();
        int sum = 0;
        smap.put(0, 1);
        int total = 0;
        for (int i = 0; i < nums.length; ++i) {
            sum += nums[i];
            int target = sum - k;
            if (smap.containsKey(target)) total += smap.get(target);
            if (!smap.containsKey(sum)) smap.put(sum, 1);
            else smap.put(sum, smap.get(sum) + 1);
        }
        return total;
    }
}