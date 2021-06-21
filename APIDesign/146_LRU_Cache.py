'''146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

'''

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