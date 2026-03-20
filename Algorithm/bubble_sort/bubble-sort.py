import time
import random
start_time = time.time()

def bubble_sort(element):
    size = len(element)

    for i in range(size - 1):
        swaped = False
        for j in range(size - 1):
            if element[j] > element[j + 1]:
                tem = element[j]
                element[j] = element[j + 1]
                element[j + 1] = tem
                swaped = True
        if not swaped : break


needToSort =  [random.randint(1, 10000) for _ in range(10000)] #rata rata selesai dalam 17,5 - 19 detik (di laptop ku)
bubble_sort(needToSort)
print(needToSort)

end_time = time.time()
duration = end_time - start_time

print(f"waktu yang di perlukan: ${duration} ")




#penjelasan kode in simple way
# arr = [2,1]
# tem = arr[0] --variable simpanan
# arr[0] = arr[1] --mengubah value dari index 0 menjadi value dari index 1
# arr[1] = tem -- mengubah value dari index 1 menjadi value dari index 0
                    # jadi mereka tempat nya bertukar

# print(arr)