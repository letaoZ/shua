/*
74. Search a 2D Matrix
Medium

8875

293

Add to List

Share
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
*/


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // flatten the matrix
        int m = matrix.size(), n = matrix[0].size();
        int l = 0, r = m * n;

        while (l < r) {
            int mid = l + (r - l) / 2;
            int i = mid / n;
            int j = mid - n * i;
            
            if (matrix[i][j] == target) // this check can be handled by outside while using l
                return true;
            else if (matrix[i][j] >= target)
                r = mid;
            else
                l = mid + 1;
        }
        int i = l / n;
        int j = l - n * i;
        if (l >= m * n || matrix[i][j] != target)
            return false;
        return true;
    }
};