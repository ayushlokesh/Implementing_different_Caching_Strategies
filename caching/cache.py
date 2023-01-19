from memory import Memory
import utilities

# This class simply adds a variable that will keep track of cache
# hits. This should be incremented in a subclass whenever the cache is
# hit.
class AbstractCache(Memory):
    def name(self):
        return "Cache"

    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache_hit_count = 0

    # Returns information on the number of cache hit counts
    def get_cache_hit_count(self):
        # In this class, always returns 0 as there is no cache.
        return self.cache_hit_count
    
class CyclicCache(AbstractCache):
    def name(self):
        return "Cyclic"

    # Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with the given cache size. You
    # can use additional methods and variables as you see fit as long
    # as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)

class LRUCache(AbstractCache):
    def name(self):
        return "LRU"

    # Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)

class RandomCache(AbstractCache):
    def name(self):
        return "Random"

    # Edit the code below to provide an implementation of a cache that
    # uses a random eviction strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
