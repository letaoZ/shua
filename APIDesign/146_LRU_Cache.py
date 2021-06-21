import collections
class LRUCache:
    ## keep track of previous and next
    ## head/tail
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.previous = {}
        self.next = {}
        self.previous['T'] = {'H'}
        self.next['H'] = 'T'
        self.cache = {}

    def get(self, key: int) -> int:
        val = -1
        # print(self.next)
        # print(self.previous)
        if key in self.cache:
            val = self.cache[key]
        
            prev = self.previous[key]
            nxt = self.next[key]
            if prev!='H':
                self.next[prev] = nxt
                self.previous[nxt] = prev
                self.previous[key] = 'H'
                self.next[key] = self.next['H']
                self.previous[self.next['H']] = key
                self.next['H'] = key
        
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.cache[key] = value
            return
        
        leaf = self.previous['T']
        while len(self.cache)>=self.capacity and leaf!='H':
            del self.cache[leaf]
            prev = self.previous[leaf]
            self.next[prev] = 'T'
            self.previous['T'] = prev
            del self.next[leaf]
            del self.previous[leaf]
            leaf = prev
            

        self.cache[key] = value
        nxt = self.next['H']
        self.next['H'] = key
        self.previous[nxt] = key
        self.next[key] = nxt
        self.previous[key] = 'H'


class LRUCache_ordereddict:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.cache[key] = value
            return
        while len(self.cache)>=self.capacity:
            for k,_ in self.cache.items():
                del self.cache[k]
                break
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)