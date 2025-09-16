class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

# Testing LRUCache

obj = LRUCache(2)

obj.put(1, 1)       # cache = {1=1}
obj.put(2, 2)       # cache = {1=1, 2=2}

print(obj.get(1))   # returns 1 (cache = {2=2, 1=1})

obj.put(3, 3)       # evicts key 2 (cache = {1=1, 3=3})
print(obj.get(2))   # returns -1 (not found)

obj.put(4, 4)       # evicts key 1 (cache = {3=3, 4=4})
print(obj.get(1))   # returns -1 (not found)
print(obj.get(3))   # returns 3
print(obj.get(4))   # returns 4
