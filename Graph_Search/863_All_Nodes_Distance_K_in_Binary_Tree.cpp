/* 
863. All Nodes Distance K in Binary Tree
Medium

5316

111

Add to List

Share
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        map<int, set<int> > g;
        queue<TreeNode *> q;
        q.push(root);
        while(!q.empty()){
            int L = q.size();
            for(int i=0; i<L; ++i){
                TreeNode * t = q.front();
                q.pop();
                if (t->left){
                    g[t->val].insert(t->left->val);
                    g[t->left->val].insert(t->val);
                    q.push(t->left);
                }
                if (t->right){
                    g[t->val].insert(t->right->val);
                    g[t->right->val].insert(t->val);
                    q.push(t->right);
                }
            }
            
        }
        // for (auto mm:g){
        //     cout<<"g:"<<mm.first<<endl;
        //     for (auto ss:mm.second)
        //         cout<<ss<<',';
        //     cout<<endl;
        // }
        queue<int> qint;
        set<int> visited;
        
        qint.push(target->val);
        visited.insert(target->val);
        while (!qint.empty() && k>0) {
            int L = qint.size();
            for (int i=0; i<L; ++i){
                int node = qint.front();
                qint.pop();
                for (auto a:g[node]){
                    if (visited.find(a) == visited.end()){
                        visited.insert(a);
                        qint.push(a);
                    }
                        
                }
            }
             k -= 1;   

        }
        
        if (qint.empty()){
            vector<int> res;
            return res;
        }
        vector<int> res(qint.size());
        int idx = 0;
        while (!qint.empty()){
            res[idx] = qint.front();
            qint.pop();
            idx += 1;
        }
        return res;
    }
};