
def linear_search(numberList, numberToFind):
    for index, value in enumerate(numberList):
        if value == numberToFind:
            return f"{index}"
            break


def binary_search(numberList, numberToFind):
    leftIndex = 0
    rightIndex = len(numberList) - 1
    midIndex = 0

    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2
        midNumber = numberList[midIndex]
        if midNumber == numberToFind:
            return midIndex

        if midNumber < numberToFind:
            leftIndex = midIndex+1
        else:
            rightIndex = midIndex -1 


arr = []
for i in range(10000):
    arr.append(i)

target = 8900

print(binary_search(arr,target))
print(linear_search(arr,target))