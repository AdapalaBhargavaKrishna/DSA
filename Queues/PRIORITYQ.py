class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def enqueue(self, value):
        self.heap.append(value) 
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def dequeue(self):
        if len(self.heap) == 0:
            return None  
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):

        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:

            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)


    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


pq = PriorityQueue()
pq.enqueue(3)
pq.enqueue(5)
pq.enqueue(1)
pq.enqueue(4)
print("Top element:", pq.peek())
print("Popped:", pq.dequeue())
print("Top element after pop:", pq.peek())
pq.enqueue(2)
print("Popped:", pq.dequeue())
print("Top element after pop:", pq.peek())