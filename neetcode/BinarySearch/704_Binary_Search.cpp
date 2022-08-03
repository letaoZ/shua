/*
704. Binary Search
Easy

5851

137

Add to List

Share
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
*/

class Solution {
public:
    int search1(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size();
        // check equal inside while
        while (l < r){
            int mid = l + (r - l) / 2;
            if (target < nums[mid])
                r = mid ;
            else if (target == nums[mid])
                return mid;
            else
                l = mid + 1;
        }
        return -1;
    }
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size();
        // check equal outside while
        while (l < r){
            int mid = l + (r - l) / 2;
            if (target <= nums[mid])
                r = mid ;
            else
                l = mid + 1;
        }
        if (l < nums.size() && nums[l] == target) return l;
        return -1;
    }
};