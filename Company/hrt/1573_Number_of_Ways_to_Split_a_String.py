'''
1573. Number of Ways to Split a String
Medium

383

53

Add to List

Share
Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.

Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
Example 2:

Input: s = "1001"
Output: 0
Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.
'''












class Solution:
    def numWays(self, s: str) -> int:
        N = len(s)
        if N<3:
            return 0
        
        M = int(1e9 + 7)
        if '1' not in s:
            ## len(s) - 1 choose 2
            Nt = N % M
            return int( ((Nt-1)*(Nt-2) // 2) % M )
        ones = sum([1 for ss in s if ss=='1'])
        
        if ones%3!=0:
            return 0
        
        ones = ones//3
        
        ## first serving with start somewhere with total ones
        ## last serving will start somewhere with total ones
        ## so we just need to cnt zeros between the bounds
        
        
        ## bar1
        idx1_left = idx1_right=None
        cnt1 = 0
        for i in range(N):
            if s[i] == '1':
                cnt1 += 1
            if cnt1 == ones:
                idx1_left = i ## bar1 must be after idx1_left
                break
                
        for i in range(idx1_left+1, N):
            
            if s[i] == '0':
                
                continue
            idx1_right = i ## bar1 must be before idx1_right
            break
            

        ## bar2
        idx2_left = idx2_right=None
        cnt2 = 0
        for i in range(N-1,-1,-1):
            if s[i] == '1':
                cnt2 += 1
            if cnt2 == ones:
                idx2_right = i ## bar2 must be before idx2_right
                break
                
        for i in range(idx2_right-1,-1,-1):
            if s[i] == '0':
                
                continue
            idx2_left = i ## bar2 must be after idx2_left
            break
        print(f"1: left, right {idx1_left} {idx1_right}")
        print(f"2: left, right {idx2_left} {idx2_right}")
        
        return int( ( ( (idx1_right - idx1_left) % M) *((idx2_right-idx2_left) % M) )  % M )
        