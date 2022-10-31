class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderdDict exposes useful methods for manipulating the cache
        # Moreover, adding a new element behaves like a list.append()
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        res = self.cache[key]
        self.cache.move_to_end(key)
        return res
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            del self.cache[key] # First deleting, then the new element will be add 
                                # at the end of the dict, respecting LRU rule
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)