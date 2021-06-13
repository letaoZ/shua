// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
    Integer cache = null;
	Iterator<Integer> iter;
    public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
        this.iter = iterator;	    
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if (cache != null) return cache;
        
        if (this.iter.hasNext()) {
            cache = this.iter.next();
            return cache;
        }
        
        return null;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    if (cache != null) {
            int ret = cache;
            cache = null;
            return ret;
        }
        
        return this.iter.next();
	}
	
	@Override
	public boolean hasNext() {
	    return cache != null || this.iter.hasNext();
	}
}