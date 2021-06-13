class RandomizedCollection {
    
    private ArrayList<Integer> list;
    private HashMap<Integer, HashSet<Integer>> map;
    private Random rand;
    /** Initialize your data structure here. */
    public RandomizedCollection() {
        this.list = new ArrayList<Integer>();
        this.map = new HashMap<>();
        this.rand = new Random();
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        if (!map.containsKey(val)) map.put(val, new HashSet<Integer>());
        
        map.get(val).add(list.size());
        list.add(val);
        
        return map.get(val).size() == 1;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        if (!map.containsKey(val) || map.get(val).isEmpty()) return false;
        
        HashSet<Integer> set = map.get(val);
        int index = set.iterator().next();
        int size = this.list.size();
        int last = this.list.get(size - 1);
        
        if (index == size - 1) {
            set.remove(index);
        } else if (val == last) {
            set.remove(size - 1);
        } else {
            set.remove(index);
            map.get(last).remove(size - 1);
            map.get(last).add(index);
            this.list.set(index, last);
        }
        
        
        
        this.list.remove(size - 1);
                
        return true;
    }
    
    /** Get a random element from the collection. */
    public int getRandom() {
        return this.list.get(rand.nextInt(this.list.size()));
    }

    public boolean removeEarlyAttemptWrongAnswer(int val) {
        if (!map.containsKey(val) || map.get(val).isEmpty()) return false;
        
        HashSet<Integer> set = map.get(val);
        int index = set.iterator().next();
        int size = this.list.size();
        int last = this.list.get(size - 1);
        
        set.remove(index);
        this.list.set(index, last);
        
        // The sequence of the following two lines matters! If remove happens first, the hash set can be empty due to
        // previous remove operation. 
        // e.g. Inert(0), Remove(0), ...,
        map.get(last).remove(size - 1);
        map.get(last).add(index);
        
        this.list.remove(size - 1);
                
        return true;
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */