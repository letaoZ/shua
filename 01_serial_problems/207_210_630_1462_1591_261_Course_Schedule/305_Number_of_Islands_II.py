import collections
List = list

## to build a whole UF graph from list of edges
## time: O(V+E*log*V)
class UF(object):
    ## V = number of nodes
    def __init__(self):
        self.id = {} 
        self.sz = {}
        self.count = 0 ## number of componnets
    
    def add(self, p):
        if p not in self.id:
            self.id[p] = p
            self.sz[p] = 1
            self.count += 1
        
    def root(self,p):
        ## time: O(log*V)
        while p!=self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
            
        return p
    def union(self,p,q):
        ## time: O(log*V)
        rtp = self.root(p)
        rtq = self.root(q)
        if rtp == rtq:
            return
        szp = self.sz[rtp]
        szq = self.sz[rtq]
        if szp>szq: ## attach smaller tree to the larger one
            szp, szq = szq, szp
            rtp, rtq = rtq, rtp
            
        self.id[rtp] = rtq
        self.sz[rtq] += szp
        self.count -= 1
        
    def isConnected(self, p,q):
        rtp = self.root(p)
        rtq = self.root(q)
        if rtp == rtq:
            return True
        return False
        
    def get_count(self):
        return self.count
    
class Solution:
    def numIslands2(
        self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        res = [0]*len(positions)
        
        g = UF()
        for i, (a,b) in enumerate(positions):
            g.add( (a,b) )
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                a1, b1 = a+dx, b +dy
                if a1<0 or b1<0 or a1>=m or b1>= n:
                    continue
                if (a1,b1) not in g.id:
                    continue
                g.union( (a,b),(a1,b1))
            res[i] = g.get_count()
            
        return res



m = 2;
n = 2;
positions = [[0,0],[1,1]];
solu = Solution()
solu.numIslands2(
    m,n, positions
)