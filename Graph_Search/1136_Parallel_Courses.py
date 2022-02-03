'''
1136. Parallel Courses
Medium

619

18

Add to List

Share
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

 

Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
 

Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
'''

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        ## build course graph
        
        g = collections.defaultdict(set)
        indegree = collections.defaultdict(int)

        for a,b in relations:
            g[a].add(b)
            indegree[b] += 1
        
        ## find the longest path and detect cycles

        ## no cycle in the graph, so we can start searching for longest path
        ## starting from ending course, i.e. the course you take in the last semester
        
        
        queue = collections.deque()
        for node in range(1,n+1):
            if indegree[node] == 0: ## i.e. a nodes we must start with
                queue.append(node)
                indegree[node] -= 1
        
        length = 0
        # print(queue)
        while queue:
            L = len(queue)
            length += 1
            for _ in range(L):
                node = queue.popleft()
                n -= 1
                ## NOTE: if not is not in g, that means it has no prerequisit,
                ## we will naturally skip them as g[node] is empty
                for next_course in g[node]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        queue.append(next_course)
            # print(queue)
        ## NOTE: if not all courses are taken, then there must be cycles
        ## a cycle can have all in degree == 1 and cannot be added to the queue using indegree == 0 condition
        return length if n==0 else -1
    
    
    
    def minimumSemesters_dfs_bfs(self, n: int, relations: List[List[int]]) -> int:
        
        ## dfs search for cycle takes too long
        ## build course graph
        
        g = collections.defaultdict(set)
        indegree = collections.defaultdict(int)

        for a,b in relations:
            g[a].add(b)
            indegree[b] += 1
        
        ## find the longest path and detect cycles
        
        
        ## start from nodes that has no sub nodes
        ## those ones are the ones to start
        
        ## dfs for cycle detection
        visited = [0]*(n+1) ## visited[i] == 1, visiting; ==2 finished visiting
        def dfs(node):
            if visited[node] == 1:
                return False
            
            visited[node] = 1
            
            
            for w in g[node]:
                if not dfs(w):
                    return False
            
            visited[node] = 2
            return True
        
        for node in range(1, n+1):
            if node not in g:
                continue
            if visited[node] == 2:
                continue
                
            if not dfs(node):
                return -1
        
        ## no cycle in the graph, so we can start searching for longest path
        ## starting from ending course, i.e. the course you take in the last semester
        
        
        queue = collections.deque()
        for node in range(1,n+1):
            if indegree[node] == 0: ## i.e. a nodes we must start with
                queue.append(node)
                indegree[node] -= 1
        
        length = 0
        # print(queue)
        while queue:
            L = len(queue)
            length += 1
            for _ in range(L):
                node = queue.popleft()
                
                ## NOTE: if not is not in g, that means it has no prerequisit,
                ## we will naturally skip them as g[node] is empty
                for next_course in g[node]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        queue.append(next_course)
            # print(queue)
        return length