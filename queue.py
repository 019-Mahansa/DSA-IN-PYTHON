#first in first out (FIFO)

#queue using list
queue_list = []
queue_list.insert(0,1) # add start from zeroo -> [1]
queue_list.insert(0,2) # nambah di 0 berarti -> [2,1]
queue_list.insert(0,3) # nambah di 0 berarti -> [3,2,1]
queue_list.insert(0,4) # nambah di 0 berarti -> [4,3,2,1]

print(queue_list.pop())
print(queue_list)
print("\n")

#queue using collection deque
from collections import deque
queque = deque()
queque.appendleft(1)
queque.appendleft(2)
queque.appendleft(3)
queque.appendleft(4)
print(queque.pop())
print(queque)

#practice



# print("This message is printed immediately.")
# time.sleep(3) # Pauses the program for 3 seconds
# print("This message is printed after a 3-second delay.")

#Queue di buat dengan Class : 
class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size (self):
        return len(self.buffer)


pq = Queue()

pq.enqueue("pizza")

pq.enqueue("mac")

print(pq.dequeue())
print(pq.dequeue())