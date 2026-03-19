import time
from collections import deque

qu = deque()
def order(n):
    for i in n:
        qu.append(i)
        time.sleep(0.5)
        print(f"{qu} order saat ini")
        print("\n")

def served():
    while qu:
        time.sleep(2)
        print(f"{qu.popleft()} sudah selesai di served")

order(["pizza","burger","spageti","sausage"])
served()
