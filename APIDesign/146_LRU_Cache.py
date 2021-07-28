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
    ## recently used!! SO, you don't need to count the number of times it is used

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




class Node:
    def __init__(self, prev = None, nxt = None, key = None):
        self.previous = prev
        self.next = nxt
        self.key = key


class LRUCache_useNode:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.data = {}## key:value pair
        self.nodes = { } ## key: node pair 
        head = Node(None,None,'H')
        tail = Node(None,None,'T')
        head.next = tail
        tail.previous = head
        self.nodes['H'] = head
        self.nodes['T'] = tail

    def print_nodes(self):
        node = self.nodes['H']
        while node is not None:
            print(node.key)
            node = node.next

    def get(self, key: int) -> int:
        # print('get')
        # print(key)
        # print(self.data)
        # (self.print_nodes())
        if key in self.data:
            val = self.data[key]
            node = self.nodes[key]
            nxt = node.next
            prev = node.previous
            
            
            prev.next = nxt
            nxt.previous = prev
            
            node.next = self.nodes['H'].next
            self.nodes['H'].next.previous = node
            self.nodes['H'].next = node
            node.previous = self.nodes['H']

        else:
            val =  -1
        

        return val
    def put(self, key: int, value: int) -> None:
        # print('put')
        # print(key,value)
        # print(self.data)
        # (self.print_nodes())
        # print('done')
        if self.capacity == 0:
            return 
        if key in self.data:
            self.get(key)
            self.data[key] = value
            return
        if len(self.data) == self.capacity:
            tail = self.nodes['T']
            to_delete = tail.previous
            # print(to_delete.key)
            # print(to_delete.previous.key)
            # print(to_delete.next.key)
            to_delete.previous.next = tail
            tail.previous = to_delete.previous
            
            del_key = to_delete.key
            
            del self.data[del_key]
            del self.nodes[del_key]
            
        new_node=Node(None,None,key)
        head = self.nodes['H']
        new_node.next = head.next
        new_node.previous = head
        head.next.previous = new_node
        head.next = new_node
        self.data[key] = value
        self.nodes[key] = new_node
        # print(self.nodes.keys())
        # self.print_nodes()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)