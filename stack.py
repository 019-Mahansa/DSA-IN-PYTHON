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


#latihan revers string using stack

def reverse(text):#pertama kali coba
    las = list(text)
    reversList = []
    for i in range(len(las)):
        nama = las.pop()
        reversList.append(nama)
    gabung = "".join(reversList)
    return gabung


print(reverse("nama ku ikbal"))

#percobaan ke dua lebih ringkas
def reversed(text):
    stacks = list(text)
    nilai = ""

    while stacks:
        nilai += stacks.pop()
    return nilai

print(reversed("dua kali coba"))