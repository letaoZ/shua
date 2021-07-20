'''
Summary:
1. If weights all > 0, i.e. triangular inequality is true, (d(u,v) + d(v,w) >= d(u,w) ), 
    then we can use dijstra
2. If some weight < 0, i.e. triangular inequality might not be true for some v (
    d(u,v) + d(v,w) < d(u,w) ), then we can use Bellman
    a: if there isn't cycle in the graph, we can topological sort Bellman ford
    b: if there is a cycle in the graph, we use Bellman ford
    
'''

import collections
import warnings
import numpy as np
class shortestPathBase(object):
    def __init__(self,n, start_point, weight_op = 's', wt_process=None):
        self.n = n
        self.g = collections.defaultdict(dict)
        self.d = {}
        self.parent = {}
        self.weight_op_s = weight_op
        self.wt_process = wt_process
        self.start_point = start_point

        ## initialize shortest distance so far
        self.d = {i:float('inf') for i in range(n)}
        if weight_op == 's':
            self.d[start_point] = 0
        elif weight_op == 'p':
            self.d[start_point] = 1

    def add_edge(self,a,b,w): ## from a to b
        if self.wt_process == 'log':
            self.g[a][b] = np.log(w)
        elif self.wt_process == 'rev':
            self.g[a][b] = 1/w
        else:
            self.g[a][b] = w

    def weight_op(self,w1,w2):
        if self.weight_op_s == "p":
            # if w1 == float('inf') :
            #     return w1*np.sign(w2)
        
            # if w2 == float('inf') :
            #     return w2*np.sign(w1)
            return w1*w2

        if self.weight_op_s == "s":

            return w1+w2

class Bellman(shortestPathBase):
    def __init__(self,n,start_point, weight_op = "s", wt_process = None):
        super().__init__(n,start_point, weight_op, wt_process)




    def solve_cyclic(self):
        ## speed O(EV)
        ## shortest distance 
        ## For each vertex, apply relaxation for all the edges
        g = self.g
        for _ in range(self.n-1):
            for i in range(self.n):
                for j in range(self.n):
                    if i in g and j in g[i]:

                        print("d[i] ", self.d[i])
                        print("self.g[i][j] ", self.g[i][j])
                        new_wt = self.weight_op(self.d[i], self.g[i][j])

                        if new_wt < self.d[j]:
                            self.d[j] = new_wt
                            self.parent[j] = i

        ## Run algorithm a second time to detect which nodes are part
        ## of a negative cycle. A negative cycle has occurred if we
        ## can find a better path beyond the optimal solution.
        for _ in range(self.n-1):
            for i in range(self.n):
                for j in range(self.n):
                    if i in g and j in g[i]:
                        new_wt = self.weight_op(self.d[i], self.g[i][j])
                        print(new_wt)
                        if new_wt < self.d[j]:
                            self.d[j] = (-float('inf') if self.weight_op_s == 's' else 0) 
                            self.parent[j] = -1 ## no parent


    def solve_dag(self):
        ## topological sort first
        ## then visit node following topological order

        def dfs(w, graph, visited, res):
            if visited[w] == 1:
                return True
            if visited[w] == 2:
                return False ## has a cycle, not acyclic
            visited[w] = 2
            for v in graph[w]:
                if not dfs(v,graph,visited,res):
                    return False
            
            visited[w] = 1
            res.appendleft(w)



        visited = [0]*self.n
        sorted_nodes = collections.deque() ## for top order
        flag = True
        for v in self.g:
            if visited[v]:
                continue
            flag = dfs(v,self.g,visited,sorted_nodes)
            if not flag:
                break
        if not flag:
            warnings.warn("graph is cyclic, switch to BellMan Ford cyclic method")
            self.solve_cyclic()
            return

        ## for each vertex u ∈ V taken in topological order
        # for each edge originating at u, (u, v) ∈ E
        # Relax(u, v)
        while sorted_nodes:
            u = sorted_nodes.popleft()
            for v in g[u]:
                # print("d[u] ", d[u])
                # print("self.g[u][v] ", self.g[u][v])
                new_wt = self.weight_op(d[u], self.g[u][v])
                if new_wt < d[v]:
                    self.d[v] = new_wt
                    self.parent[v] = u



'''
0 ---> 1 --> 2 
    1/2    2/8
0 --->4 --> 1
    1/10    2   
'''

## DAG case both solve cyclic and solve dag work
x = Bellman(5,0,weight_op='p')
x.add_edge(0,1,1/2)
x.add_edge(1,2,2/8)
x.add_edge(0,4,1/10)
x.add_edge(4,1,2.)
# x.solve_cyclic()
x.solve_dag()




'''
0 ---> 1 --> 2 --->1
    1/2    2/8  1
0 --->4 ---> 1 
    1/10   2    
'''

## DAG case both solve cyclic and solve dag work
x = Bellman(5,0,weight_op='p')
x.add_edge(0,1,1/2)
x.add_edge(1,2,2/8)
x.add_edge(0,4,1/10)
x.add_edge(4,1,1.)
x.add_edge(2,1,1) ## make the graph cyclic
# x.solve_cyclic()
x.solve_dag()
x.d





'''
0 ---> 1 --> 2 
  (1/2)   2/8
0 --->4 --> 1
    1/10    2   
'''

## DAG case both solve cyclic and solve dag work
## use log sum
x = Bellman(5,0,weight_op='s', wt_process='log')
x.add_edge(0,1,1/2)
x.add_edge(1,2,2/8)
x.add_edge(0,4,1/10)
x.add_edge(4,1,2.)
x.solve_cyclic()
#x.solve_dag()
x.d

