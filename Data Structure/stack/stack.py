#stack is last in first out

#using a list
s = []
s.append("minecraft")
s.append("Skycrim")
s.append("Forza horizon")
s.append("Amazon")

print(s)
print(f"Menghapus bagian paling atas {s.pop()}")
print(s)
print("\n")

#using deque
from collections import deque
stack = deque()
stack.append("Minecraft")
stack.append("Skycrim")
stack.append("Forza Horizon")
stack.append("Amazon")

print(stack)
print(f"Menghilangkan bagian paling atas: {stack.pop()}")
print(stack)


