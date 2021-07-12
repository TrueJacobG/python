class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        tempHead = self.head
        while tempHead:
            print(tempHead.data)
            tempHead = tempHead.next


linkedList = LinkedList()
linkedList.head = Node(1)
secondElement = Node(2)
thirdElement = Node(3)

linkedList.head.next = secondElement
secondElement.next = thirdElement

linkedList.printLinkedList()
