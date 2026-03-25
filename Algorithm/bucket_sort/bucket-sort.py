import time
import random
start_time = time.time()

def insertionSort(n):
    for i in range(len(n)):
        anchor = n[i]
        j = i - 1
        while j >= 0 and anchor < n[j]:
            n[j + 1] = n[j]
            j = j-1
        n[j+1] = anchor


def bucketSort(n:list):
    bucket = []
    length = len(n)

    for i in range(len(n)):
        bucket.append([])

    max_val = max(n)
    for i in n:
        normalized = i / (max_val + 1)
        bucketNo = int(length * normalized)
        bucket[bucketNo].append(i)
    
    for bu in bucket:
        insertionSort(bu)
    output = []
    for bu in bucket:
        output.extend(bu)
    return output
end_time = time.time()


needTo = [random.randint(1, 10000) for _ in range(10000)] #2,5 - 3 s
print(bucketSort(needTo))
print(f"{end_time - start_time} second")