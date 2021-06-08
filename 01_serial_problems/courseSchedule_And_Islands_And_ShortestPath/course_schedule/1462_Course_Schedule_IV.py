'''
1462. Course Schedule IV
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether the course uj is a prerequisite of the course vj or not. Note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

Return a boolean array answer, where answer[j] is the answer of the jth query.

 

Example 1:


Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.
Example 3:


Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
 

Constraints:

2 <= numCourses <= 100
0 <= prerequisite.length <= (numCourses * (numCourses - 1) / 2)
0 <= ai, bi < n
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 104
0 <= ui, vi < n
ui != vi

'''

import collections

List = list()

class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ## most recent submission: 2021/06/08
        g = collections.defaultdict(set)
        cand = set()
        for a, b in prerequisites:
            g[b].add(a)
            cand.add(a)
            cand.add(b)
            
        adjmat = {a:{b:False for b in cand } for a in cand }
        visited = [[0]*numCourses for _ in range(numCourses)]
        for a,b in prerequisites:
            adjmat[b][a] = True
            
        def searching(cand,frm,t,adjmat):
            if visited[frm][t]:
                return adjmat[frm][t]
            visited[frm][t] = True
            for k in cand:
                if k==frm or k==t: continue
                adjmat[frm][t] =(
                    adjmat[frm][t] or 
                    (searching(cand,frm,k,adjmat) and searching(cand,k,t,adjmat) )
                )
            return adjmat[frm][t] 
        
        
        res =[False]*len(queries)
        for ii, (t, frm) in enumerate(queries):
            if t not in cand or frm not in cand:
                res[ii] = False
                continue
            res[ii] = searching(cand,frm,t,adjmat)
                
            
        return res

    def checkIfPrerequisite_cache_ALL_path(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    
        def searching(reachable,candidates):
            
            for k in candidates:
                for i in candidates:
                    for j in candidates:
                        reachable[i][j] = reachable[i][j] or (
                            reachable[i][k] and reachable[k][j])
            
            return reachable
        
        if not prerequisites:
            return [False]*len(queries)
        
        adjMatrix =  [[ 0 ]*n for _ in range(n)]
        candidates = [0]*n
        for a,b in prerequisites:
            adjMatrix[a][b] = 1
            candidates[a] = 1
            candidates[b] = 1
            
        candidates = [idx for idx,val in enumerate(candidates) if val==1]
        ans = []
        searching(adjMatrix, candidates)
        for a,b in queries:
            ans.append(bool(adjMatrix[a][b]))
        
        return ans
            

    def checkIfPrerequisite_dfs(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        
        
        def searching(g,v,visited, target):
            
            if target in g[v]: 
                # fromTo[v] = target
                return True
            if visited[v] == 1:
                return False
            
            visited[v] = 1
            
            for w in g[v]:
                if searching(g,w,visited, target):
                    return True
            return False
        
        ## build graph
        ## dfs for connected components and keep track of path
        ## fromTo[b][a] -- to reach a from b
        ## scc[a] -- label strong connect component for a
        
        if len(prerequisites) == 0:
            return [False]*len(queries)
        
        g = collections.defaultdict(set)

        for a,b in prerequisites:
            g[b].add(a)

        res = [False]*len(queries)
        for i in range( len(queries) ):
            a, b = queries[i]
            visited =[0]*numCourses
            
            res[i] = searching(g,b,visited, a)
        return res
            
            
            
        
    def checkIfPrerequisite_dfs_topSort_Scc(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        
        ## dfs: find strongly connect components
        ## return topological sort
        ## if a,b in the same components and a before b, then a is a prerequired
        ##
        
        
        def searching(g,v,visited,topOrd, scc, tag):

            if visited[v] == 1:
                return 
            
            visited[v] = 1
            scc[v] = tag
            for w in g[v]:
                searching(g,w,visited,topOrd, scc, tag)
            topOrd.append(v)
            return False
        
        ## build graph
        ## dfs for connected components and keep track of path
        ## scc[a] -- label strong connect component for a
        ## topOrd -- topological order
        
        if len(prerequisites) == 0:
            return [False]*len(queries)
        
        g = collections.defaultdict(set)
        visited = [-1]*numCourses
        for a,b in prerequisites:
            g[b].add(a)
            visited[a] = visited[b] = 0

        scc = [-1]*numCourses
        topOrd = []
        tag = 1
        
        for w in range(numCourses):
            if visited[w] == 0:
                searching(g,w,visited,topOrd, scc, tag)
                tag += 1        
            
        topOrd = topOrd[::-1]
        res = [False]*len(queries)
        print(topOrd)
        print(scc)
        for i in range( len(queries) ):
            a, b = queries[i]
            # if a==b or scc[a]!=scc[b]: continue
            ida = topOrd.index(a)
            idb = topOrd.index(b)
            if ida<idb:
                res[i] = True

        return res
            
            