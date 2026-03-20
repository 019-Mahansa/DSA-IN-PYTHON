import time
import random
start_time = time.time()
def insertionSort(element):
    for i in range(1, len(element)):
        anchor = element[i]
        j = i-1
        while j >= 0 and anchor < element[j]:
            element[j + 1] = element[j]
            j = j -1
        element[j+1] = anchor

def run_median(stream):
    arr = []

    for i in stream:
        arr.append(i)
        insertionSort(arr)

        n = len(arr)
        if n % 2 == 1:
            median = arr[n // 2]
        else:
            median = (arr[n // 2] + arr[n // 2 - 1]) / 2
        print(median)



needToSorted = [random.randint(1, 10000) for _ in range(10000)] 
# insertionSort(needToSorted)
run_median(needToSorted)
print(needToSorted)

end_time = time.time()
duration = end_time - start_time

print(f"waktu yang di perlukan: ${duration} ")