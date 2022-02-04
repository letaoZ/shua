class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
        vector<int> pre(n); // pre[i]: the bit representation of all dependencies of course i
        for(auto& e : dependencies){
            e[0] -= 1;
            e[1] -= 1;
            pre[e[1]] |= 1 << e[0];
        }
        cout<<"vector"<<endl;
        for(int i=0; i<n; ++i)
            cout<<pre[i]<<", ";
        cout<<endl;
        // i is the bit representation of a combination of courses. 
        // dp[i] is the minimum days to complete all courses in i's representation
        vector<int> dp(1 << n, n); 
        // no need time to finish 0 courses
        dp[0] = 0;
        cout<<endl;
        for(int i = 0; i < (1 << n); i += 1){
            cout<<"courses "<<i<<endl;
            cout<<"dp : "<<dp[i]<<endl;
            int ex = 0;
            // find  out ex, the bit representation of the all courses that we can study now.
            // since we have i and pre[j], we know course j can be studied if i contains all it's prerequisites ((i & pre[j]) == pre[j])
            for(int j = 0; j < n; j += 1) if((i & pre[j]) == pre[j]) ex |= 1 << j;
            // we don't want to study anything from what we have already studied (i represents set of courses that we have studied)
            ex &= ~i; 
            cout<<"need to take: "<<ex<<endl;
           // enumerate all the bit 1 combinations of ex
           // this is a typical method to enumerate all subsets of a bit representation:
           // for (int i = s; i; i = (i - 1) &ｓ)
           // __builtin_popcount counts bits == 1 
            for(int s = ex; s; s = (s - 1) & ex) {
                    if(__builtin_popcount(s) <= k){
                    cout<<"taking: "<<s<<endl;
                    cout<<"visit s|i: "<<(s|i)<<endl;
                    // any combination of courses (if less or equal than k) could be studied at this step
                    // i | s means what we combine already studied courses before with courses we can study at the current step
                    dp[i | s] = min(dp[i | s], dp[i] + 1);
                }
            }
            cout<<"dp : "<<dp[i]<<endl;

            cout<<endl;
        }
        // dp.back is the state when we studied all the courses. e.g. 11111...
        return dp.back(); 
    }
};