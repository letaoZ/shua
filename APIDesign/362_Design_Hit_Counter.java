class HitCounter {
    private int current = 1;
    private int sum = 0;
    private TreeMap<Integer, Integer> map;
    /** Initialize your data structure here. */
    public HitCounter() {
        map = new TreeMap<>();
        map.put(0, 0);
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        if (timestamp > current) {
            map.put(current, sum);
            current = timestamp;
        }
        sum++;
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        if (timestamp > current) {
            map.put(current, sum);
            current = timestamp;
        }
        int past = Math.max(0, timestamp - 300);
        int key = map.floorKey(past);
        return sum - map.get(key);
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */