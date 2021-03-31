

class solution:
    def shortestSuperstring(self, words):
        ## remove dup, randomize order
        words = list(set(words))


        # time: O(n)
        def dist(w1,w2):
            """distance=overlap from w1 to w2

            Args:
                w1 ([str]): word
                w2 ([str]): word
            """
            ll = max(len(w1),len(w2))
            res12 = 0
            for k in range(ll):
                if w2.startswith(w1[k:] ):
                    res12 = len(w1) -(k)
                    break
            return res12


        # time: O(len(words))
        def build_path(wws,dag, path):
            res = ""
            if not path:
                for w in wws:
                    res += w
                return res

            res = wws[path[0]]
            print(path)
            for i,j in zip(path[:-1], path[1:]):
                k = dag[i][j]
                res += wws[j][k:]
            return res


        ## weighted dir graph of words, node = word, edge weight = dist(), wt>0
        ## Find the longest paths of each connected components

        dag = collections.defaultdict(dict)
        L = len(words)

        ## time O(len(words)^2 * len(word))
        for i in range(L):
            for j in range(L):
                if i==j: dag[i][j] = 0
                
                dd = dist(words[i],words[j])
                dag[i][j] = dd


        ##keep track
        ## (i,1<<i,[i],0)
        ## ith word, visited node so far, path (with direction), path length

        Q = collections.deque([(i,1<<i,[i],0) for i in range(L)])

        ## d_set[node_set][n] -- longest path consisting of nodes_set and end with node n
        d_set = [[0]*L for _ in range(1<<L)]


        l = -1 ## current largest length
        P = [] ## current path with the largest length

        ## BFS: time O(len(words)**2)
        ##space: O(len(words)* (2**len(words))), store d_set
        while Q:
            node, node_set, path, cur_len = Q.popleft()
            if cur_len < d_set[node_set][node]:
                continue
            if node_set == (1<<L) - 1:
                if cur_len>l:
                    P, l = path, cur_len
                    continue
            for i in range(L):
                node_set_next = (node_set | (1<<i))
                ## i is already in node_set
                if node_set == node_set_next: continue

                ## current path is longer
                next_L = d_set[node_set][node] + dag[node][i]

                if  next_L<= d_set[node_set_next][i]: continue

                d_set[node_set_next][i] = next_L
                Q.append((i,node_set_next,path+[i],next_L))

        res = build_path(words,dag,P)
        print('path')
        print(P)
        return res
        


import collections
words = ["catg","ctaagt","gcta","ttca","atgcatc"]
words = ["abc","ca"]
words= ["ab"]
tester = solution()
tester.shortestSuperstring(words)

