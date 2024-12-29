from queue import Queue, LifoQueue, PriorityQueue
from collections import deque

#1. Queue
def demoqueue():

    print("Queue FIFO")

    q = Queue(maxsize=3)
    q.put(10)
    q.put(20)
    q.put(30)
    print(f"Queue after Enqueue : ", list(q.queue))
    print(f"Dequeued : ", q.get())
    print(f"Queue after Dequeue : ", list(q.queue))

#2. Lifo Queue

def lifo_queue():
    print("Lifo Queue")

    q = LifoQueue(maxsize = 3)

    q.put(10)
    q.put(20)
    q.put(30)
    print(f"queue after Enqueue : {list(q.queue)}")

    print(f"Dequeued : {q.get()}")

    print(f"queue after Dequeue : {list(q.queue)}")

def priority_queue():
    print("Priority Queue")

    pq = PriorityQueue()

    pq.put((2, "Task 2"))
    pq.put((1, "Task 1"))
    pq.put((3, "Task 3"))
 
    while not pq.empty():
        print(pq.get())

def dequeue():
    print("Deque")
    dq = deque()

    dq.append(10)
    dq.append(20)
    dq.appendleft(30)
    print("Deque after adding elements: ", list(dq))

    dq.pop()
    dq.popleft()
    print("Deque after removing elements: ", list(dq))


demoqueue()
lifo_queue()
priority_queue()
dequeue()