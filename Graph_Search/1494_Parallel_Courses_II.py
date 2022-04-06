'''
1494. Parallel Courses II
Hard

548

42

Add to List

Share
You are given an integer n, which indicates that there are n courses labeled from 1 to n. 
You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], 
representing a prerequisite relationship between course prevCoursei and course nextCoursei: 
course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.

In one semester, you can take at most k courses as long as you have taken all the prerequisites 
in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. 
The testcases will be generated such that it is possible to take every course.

 

Example 1:



Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3 
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.
Example 2:



Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4 
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3 only since you cannot take more than two per semester.
In the second semester, you can take course 4.
In the third semester, you can take course 1.
In the fourth semester, you can take course 5.
Example 3:

Input: n = 11, dependencies = [], k = 2
Output: 6
 

Constraints:

1 <= n <= 15
1 <= k <= n
0 <= relations.length <= n * (n-1) / 2
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
The given graph is a directed acyclic graph.
'''

## too slow, but passsed
## time complexity 3^n

'''

if mask m has k enabled bits, then it will have 2^k submasks.
So we have a total of C(n, k) combinations.
then the total number of combinations for all masks will be: Σ k = 0..n ( C(n, k) * 2^k )
By binomial coefficients, Σ k = 0..n ( C(n, k) * 2^k ) = (1 + 2)^n = 3^n

for (int m=0; m<(1<<n); ++m)      <= C(n, k), k = 0 to n enable bits
    for (int s=m; s; s=(s-1)&m)   <= 2^k (submasks, k enable bits of m)

'''
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        ## since n is small, we can use bitmask
        
        
        if k == 1:
            return n
        if len(relations) == 0:
            if n%k == 0:
                return n//k
            else:
                return 1+n//k
            
            
        pre = [0]*(n ) ## nodes are labeled 1--n, we change it to 0 -- n-1

        for a,b in relations:
            pre[b-1] |= (1 << (a-1) ) ## map each course to collection of its prerequired courses; node (a-1) maps to bit 2**(a-1)
            
        ## dp[i] :=  taken all courses in bits rep of i, min num of days need
        ## min days we need to finish them
        dp = [1+n]*(1 << n) 
        
        dp[0] = 0 ## we need 0 days to take 0 courses
        
        for i in range(0, 1<<n):
            if dp[i] == n+1:
                continue ## not reachable
            to_be_taken = 0 ## courses that remains to take
            for j in range(n): 
                if pre[j] & i == pre[j]: ## for each course, if its prerequisites are  in i, i.e. all taken, we add the course to "to be taken"
                    to_be_taken |= (1 << j)
                    
            ## we can also remove the courses in i from to_be_taken
            to_be_taken &= (~i)
            
            ## now, we have the max num of courses we can take each semester is k
            ## the number of "1" in binary rep of to_be_taken represent number of courses to be taken
            ## we need to loop through all sub bit1 rep of  to_be_taken, with num of "1"'s <= k, 
            ## (eg. if to_be_taken = (1,1,0), the subs are (1,1,0), (1,0,0),(0,1,0),(0,0,0))
            ## given a sub S, we can update d[i|S] = min(dp[i|S], dp[i] + 1) 
            ## here (i|S == courses i union courses S), since dp[i] represent min days we use to take all courses i; for extra S courses, it could take one extra semester to finish
            
            sub = to_be_taken
            while sub:
                # if dp[sub] == n+1:
                #     continue ## not reachable
                k_courses = sub.bit_count()
                if k_courses <= k:
                    dp[ i | sub] = min(dp[i | sub], dp[i] + 1) ## NOTE: i|sub always  >= i, so we are fine to loop through i
                    
                sub = (sub - 1) & to_be_taken ##this is a typical method to enumerate all subsets of a bit representation:

                
        return dp[-1]