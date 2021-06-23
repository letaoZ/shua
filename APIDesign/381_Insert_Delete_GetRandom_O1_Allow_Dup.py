
'''381. Insert Delete GetRandom O(1) - Duplicates allowed


Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
Output
[null, true, false, true, 2, true, 1]

Explanation
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // return True. Inserts 1 to the collection. Returns true as the collection did not contain 1.
randomizedCollection.insert(1);   // return False. Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
randomizedCollection.insert(2);   // return True. Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
randomizedCollection.remove(1);   // return True. Removes 1 from the collection, returns true. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equally likely.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105  calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

'''
import random
import collections
class RandomizedCollection:
##  set is implemented as a hash table. So you can expect to lookup/insert/delete in O(1) average. 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values =collections.deque()
        self.values_d = {}
        
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        res = True
        if val in self.values_d:
            self.values_d[val].add(len(self.values))
            res = False
        else:
            self.values_d[val] = set([len(self.values)])
            res = True
        
        self.values.append(val)
        # print('insert: ', val)
        # print(self.values)
        # print(self.values_d)
        return res
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.values_d:
            return False
        
        idx = self.values_d[val].pop()
        last_id = len(self.values) - 1
        
        if idx == last_id:
            self.values.pop()
        else:
            last_val = self.values[-1]
            self.values.pop()
            self.values_d[last_val].discard(last_id)
            
            self.values_d[last_val].add(idx)
            self.values[idx] = last_val
            
        if len(self.values_d[val]) == 0:
            del self.values_d[val]
        # print('remove: ', val)
        # print(self.values)
        # print(self.values_d)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        idx = random.randint(0,len(self.values)-1)
        return self.values[idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()