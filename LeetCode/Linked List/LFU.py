class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size > 0:
            node = self.tail.prev
            self.remove_node(node)
            return node
        return None


class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.node_map = {}
        self.freq_map = {}

    def _update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].add_node(node)

    def get(self, key):
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update_freq(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update_freq(node)
            return
        if self.size >= self.capacity:
            lfu_list = self.freq_map[self.min_freq]
            to_remove = lfu_list.remove_last()
            del self.node_map[to_remove.key]
            self.size -= 1
        new_node = Node(key, value)
        self.node_map[key] = new_node
        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()
        self.freq_map[1].add_node(new_node)
        self.min_freq = 1
        self.size += 1

# Testing LFUCache

obj = LFUCache(2)

obj.put(1, 1)       # cache = {1=1}
obj.put(2, 2)       # cache = {1=1, 2=2}

print(obj.get(1))   # returns 1 (freq of 1 becomes 2)

obj.put(3, 3)       # evicts key 2 (both 1 and 2 had freq=1, but 1 was used recently -> keep 1)
print(obj.get(2))   # returns -1 (not found)
print(obj.get(3))   # returns 3

obj.put(4, 4)       # evicts key 1 (freq of 1=2, freq of 3=1, evict LFU which is key 3)
print(obj.get(1))   # returns -1 (not found)
print(obj.get(3))   # returns 3
print(obj.get(4))   # returns 4
