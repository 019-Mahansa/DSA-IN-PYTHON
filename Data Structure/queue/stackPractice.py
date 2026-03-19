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