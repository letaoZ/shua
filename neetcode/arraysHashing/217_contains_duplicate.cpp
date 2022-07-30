#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> m;
        for (int i=0; i< nums.size(); ++i ){
            if (m.find(nums[i]) != m.end())
                return true;
            m.insert(nums[i]);
        }
        return false;
    }
};

int main(){
    return 0;
}