'''
207. Course Schedule
Medium

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
All the pairs prerequisites[i] are unique.

'''
import collections
List = list
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
## build graph
        g = collections.defaultdict(set)
        
        ## initialize to 2 just to make sure we mark all existing course
        ## some courses numbers may NOT show up in prerequisites
        visited = [2]*numCourses

        for a,b in prerequisites:
            g[b].add(a)
            visited[a] = visited[b] = 0

        def searching(visited, g, v):
            if visited[v] == -1:
                return False
            if visited[v] ==1:
                return True
            visited[v] = -1
            for w in g[v]:
                if not searching(visited,g,w):
                    return False
            visited[v] = 1
            return True
        res = True
        for v in range(numCourses):
            if visited[v]==0:
                if not searching(visited, g, v):
                    res = False
                    break
        return res
        
        
    def canFinish_assumed_courses_randomly_numbered(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = collections.defaultdict(set)
        visited =dict()
        for a,b in prerequisites:
            g[b].add(a)
            visited[a] = visited.get(a,0)
            visited[b] = visited.get(b,0)

        def searching(visited, g, v):
            if visited[v] == -1:
                return False
            if visited[v] ==1:
                return True
            visited[v] = -1
            for w in g[v]:
                if not searching(visited,g,w):
                    return False
            visited[v] = 1
            return True
        res = True
        for v in visited:
            if visited[v]==0:
                if not searching(visited, g, v):
                    res = False
                    break
        return res


solu = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]

solu.canFinish(numCourses, prerequisites)
