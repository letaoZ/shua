'''
207. Course Schedule
Medium

8307

323

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## cycle detection in directed graph
        
        
        g = collections.defaultdict(set)
        for a,b in prerequisites:
            g[b].add(a) ## an edge: b->a
            if a == b:
                return False
           
        
        visited = collections.defaultdict(int)
        ## visited[i] == 1 visiting; visited[i] == 2 finished visits; else haven't visit
        
        
        def searching(v, visited):
            if visited[v] == 1:
                return False ## cycle detected
            
            
            if visited[v] == 2:
                return True
            
            visited[v] = 1
            for w in g[v]:
                res = searching(w, visited)
                if not res:
                    return res
                
            
            visited[v] = 2 ## finished visit
            return True
        
        
        for i in range(numCourses):
            if i not in g or visited[i] == 2:
                continue
                
            res = searching(i, visited)
            if not res:
                return res
            
        return True