import heapq
l = [5, 3, 1, 8, 6, 2, 7]
heapq.heapify(l)
l #[1, 3, 2, 8, 6, 5, 7]
heapq.heappop(l) # 1
print(l) # [2, 3, 5, 8, 6, 7]
heapq.heappop(l) # 2
print(l) # [3, 6, 5, 8, 7]
heapq.heappush(l, 9)
print(l) # [3, 6, 5, 8, 7, 9]
heapq.heappush(l, 4)
print(l) # [3, 6, 4, 8, 7, 9, 5]
l = [5, 3, 1, 8, 6, 2, 7]
heapq.heapify(l)
print(l) #[1, 3, 2, 8, 6, 5, 7]
heapq.heappushpop(l, 4)
print(l) #[2, 3, 4, 8, 6, 5, 7]
l = [5, 3, 8, 6, 2, 7]
heapq.heapify(l)
print(l) #[2, 3, 7, 6, 5, 8]
l.append(1)
print(l) #[2, 3, 7, 6, 5, 8, 1]x


class PriorityQueue:
    def __init__(self):
        self.queue = []     
        self.index = 0
    def push(self, item, priority):
        
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]  
    
    def is_empty(self):
        return len(self.queue) == 0

pq = PriorityQueue()

pq.push("task1", priority=3)
pq.push("task2", priority=1)
pq.push("task3", priority=2)

print(pq.pop()) 
print(pq.pop()) 
print(pq.pop()) 
