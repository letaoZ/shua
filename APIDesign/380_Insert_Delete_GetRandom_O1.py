'''380. Insert Delete GetRandom O(1)


Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

'''

import random
import collections

class RandomizedSet:

    ## Note: for list: append and pop are both O(1)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.values_d = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        ##NOTE: a in list checking, takes O(n) time
        if val in self.values_d:
            return False
        N = len(self.values)
        self.values_d[val] = N
        self.values.append(val)
        
#         print('add',val)
#         print(self.values_d)
#         print(self.values)
        return True
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.values_d:
            return False
        
        idx = self.values_d[val]
        last_idx = len(self.values) - 1
        if idx ==last_idx:
            self.values.pop()##O(1)
            del self.values_d[val]
        else:
            last_val = self.values[last_idx]
            self.values[idx] = last_val
            self.values.pop()
            del self.values_d[val]
            self.values_d[last_val] = idx
            
#         print('remove',val)
#         print(self.values_d)
#         print(self.values)
        return True
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0,len(self.values) - 1)
        return self.values[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class Node:
    def __init__(self, previous = None, next = None,value = None):
        self.previous = previous
        self.next = next
        self.value= value
        

class RandomizedSet_dict:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = dict()## dict of nodes
        self.dummy = Node(None,None,'H')
        tail = Node(self.dummy,None,'T')
        self.dummy.next = tail
        self.values['H'] = (self.dummy, -1)
        self.values['T'] = (tail, -1)
        self.cnt = 0
        self.idx = {}
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.values:
            return False
        
        
        node = Node(None, None, val)
        node.previous = self.dummy
        node.next = self.dummy.next
        
        self.dummy.next.prevous = node
        
        self.cnt += 1
        
        self.values[val] = (node,self.cnt)
        self.idx[self.cnt] = val
        
        
        return True
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.values:
            return False
        
        
        node, idx = self.values[val]
        
        node.previous.next = node.next

        node.next.previous = node.previous
        del self.values[val]
        if idx == self.cnt:
            self.cnt -= 1
            del self.idx[idx]
            return True
        
        ## move the last value to where the removed value is
        last_val = self.idx[self.cnt]

        last_node, _= self.values[last_val]
        self.idx[idx] = last_val
        self.values[last_val] = (last_node, idx)
        
        del self.idx[self.cnt]
        self.cnt -= 1
        
        return True
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.cnt == 0:
            return -1
        
        idx = random.randint(1,self.cnt)
        return self.idx[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()