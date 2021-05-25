import collections

class Solution:
    def numDistinctIslands2(self, g: List[List[int]]) -> int:
        def dihedral(w):
            ## apply dihedral group action to each point of the polygone
            ## for each action: shift the shape to the upper left corner
            res = [[] for i in range(8)]        
            for x,y in w:
                res[0].append([x,y])
                res[1].append([x,-y])
                res[2].append([-x,y])
                res[3].append([-x,-y])   
                res[4].append([y,x])
                res[5].append([y,-x])
                res[6].append([-y,x])
                res[7].append([-y,-x]) 
            for extv in res:
                extv.sort()
                a,b = extv[0]
                for i in range(len(extv)):
                    a1,b1 = extv[i]
                    extv[i] = (a1-a, b1-b)
            res.sort()
            return tuple( tuple(t) for t in res)


        def searching(g,x,y,lands):
            if x>=M or y>=N or x<0 or y<0: return
            if g[x][y] == 0: return
                
            g[x][y] = 0
            lands.append((x,y))
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                x1,y1 = x+dx, y+dy
                
                
                searching(g,x1,y1,lands)

        ## keep track of all islands
        ## islands[k] = list of islands with k points
        ## islands[k][i] = a list of points in an island


        
        islands = collections.defaultdict(list)
        M, N = len(g), len(g[0])
        for x in range(M):
            for y in range(N):
                k = [0]
                lands = []
                if g[x][y] == 1:
                    searching(g,x,y,lands)
                    if len(lands)>0:
                        ## only lands of the same num of points could be rotational equivalent
                        islands[len(lands)].append(lands)


        nIslands = 0

        for k,v in islands.items():
            if len(v)<= 1: 
                nIslands += len(v)
                continue

            shrinkage = set()
            for w in v:
                dw = dihedral(w)
                shrinkage.add(dw)
            print(shrinkage)
            nIslands += len(shrinkage)

        return nIslands


g = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
solu = Solution()
solu.numDistinctIslands2(g)