from memory import Memory
import utilities
import random as rd

# This class simply adds a variable that will keep track of cache
# hits. This should be incremented in a subclass whenever the cache is
# hit.
class AbstractCache(Memory):
    def name(self):
        return "Cache"

    # Takes two parameters. Data is the data that forms the
    # "memory". Size is a non-negative integer that indicates the size
    # of the cache.
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache_hit_count = 0

    # Returns information on the number of cache hit counts
    def get_cache_hit_count(self):
        # TODO: Edit this code to correctly return the count of cache hits.
        return self.cache_hit_count
    
class CyclicCache(AbstractCache):
    def name(self):
        return "Cyclic"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with the given cache size. You
    # can use additional methods and variables as you see fit as long
    # as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache = [None]*size
        self.cache_memory = [None]*size
        self.size = size
        self.cycle_tracker = 0
        if self.size <= 0:
            self.size = 5

    def lookup(self, address):
        if address in self.cache:
            self.cache_hit_count += 1
            return self.cache_memory[self.cache.index(address)]
        for i in range(0,self.size):
            if self.cache[i] == None:
                self.cache[i] = address
                self.cache_memory[i] = self.memory[address]
                break
        else:
            self.cache[self.cycle_tracker] = address
            self.cache_memory[self.cycle_tracker] = self.memory[address]
            self.cycle_tracker += 1
            self.cycle_tracker = self.cycle_tracker % self.size
        return super().lookup(address)
class LRUCache(AbstractCache):
    def name(self):
        return "LRU"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache = [None]*size
        self.cache_memory = [None]*size
        self.size = size
        self.priority_tracker = [0]*size

    def lookup(self, address):
        for i in range(0,self.size):
                if self.cache[i] != address and self.cache[i] != None:
                    self.priority_tracker[i] += 1
                else:
                    self.priority_tracker[i] = 0
        if address in self.cache:
            self.cache_hit_count += 1
            return self.cache_memory[self.cache.index(address)]
        for i in range(0,self.size):
            if self.cache[i] == None:
                self.cache[i] = address
                self.cache_memory[i] = self.memory[address]
                break
        else:
            self.cache[self.priority_tracker.index(max(self.priority_tracker))] = address
            self.cache_memory[self.priority_tracker.index(max(self.priority_tracker))] = self.memory[address]
            self.priority_tracker[self.priority_tracker.index(max(self.priority_tracker))] = 0
        return super().lookup(address)
    
class RandomCache(AbstractCache):
    def name(self):
        return "Random"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a random eviction strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache = [None]*size
        self.cache_memory = [None]*size
        self.size = size

    def lookup(self, address):
        if address in self.cache:
            self.cache_hit_count += 1
            return self.cache_memory[self.cache.index(address)]
        for i in range(0,self.size):
            if self.cache[i] == None:
                self.cache[i] = address
                self.cache_memory[i] = self.memory[address]
                break
        else:
            x = rd.randint(0,4)
            self.cache[x] = address
            self.cache_memory[x] = self.memory[address]
        return super().lookup(address)
