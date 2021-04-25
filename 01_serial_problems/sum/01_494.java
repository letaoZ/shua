/**
 * DFS + Memoization. Pay extra attention to the base case! E.g. +0, -0.
 */

class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        Map<Integer, Map<Integer, Integer>> rmap = new HashMap<>();
        return dfs(target, 0, nums, rmap);
    }
    
    
    private int dfs(int target, int level, int[] nums, Map<Integer, Map<Integer, Integer>> rmap) {
        if (rmap.containsKey(level) && rmap.get(level).containsKey(target)) {
            return rmap.get(level).get(target);
        }
        
        if (level == nums.length - 1) {
            int temp = 0;
            if (nums[level] == target) temp += 1;
            if (nums[level] == -target) temp += 1;
            return temp;
        }
        
        int result = dfs(target + nums[level], level + 1, nums, rmap) + dfs(target - nums[level], level + 1, nums, rmap);
        if (!rmap.containsKey(level)) rmap.put(level, new HashMap<>());
        rmap.get(level).put(target, result);
        return result;
    }
}