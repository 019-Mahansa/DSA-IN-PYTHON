class LinkedList:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode

number1 = LinkedList("3")
number2 = LinkedList("9")
number3 = LinkedList("11")
lastNode = None

number1.nextNode = number2
number2.nextNode = number3
number3.nextNode = lastNode

curretNode = number1

while currentNode is not None:
    print(currentNode.value, "--> ", end="")
    currentNode = currentNode.nextNode

print(lastNode)