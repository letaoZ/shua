
'''
210. Course Schedule II
Medium


There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

'''
import collections
List = list
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        
        def searching(g,v,visited, path):
            if visited[v] == -1:
                return False
            if visited[v] == 1:
                return True
            visited[v] = -1
            print(v)
            for w in g[v]:
                if not searching(g,w,visited,path):
                    return False
            path.append(v)
            visited[v] = 1
            return True
        
        ## g: graph of courses. a->b , a is prerequire for b
        ## visited: courses labeled 2 means no prerequire
        g = collections.defaultdict(set)
        visited = [2]*numCourses
        for a,b in prerequisites:
            g[b].add(a)
            visited[a] = visited[b] = 0
            
        ## path: keep track of ordering
        path = []
        
        ## others: keep track for labeled 2 courses
        others = []
        res = True

        for v in range(numCourses):
            if visited[v] == 0:
                if not searching(g,v,visited,path):
                    res = False
                    break
            if visited[v] == 2:
                others.append(v)
        if res:
            path = others + path[::-1]
        else:
            path = []

        return path

numCourses = 3
prerequisites = [[1,0],[2,1],[2,0]]

## this test case can have a partial result [1,2]
numCourses = 6
prerequisites = [[2,1],[2,3],[1,3],[4,3], [5,4],[4,5]]