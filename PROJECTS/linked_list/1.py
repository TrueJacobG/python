class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        array = []
        while temp:
            array.append(temp.data)
            temp = temp.next
        print(array)
        return array

    def addOnEnd(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        temp = self.head
        while temp:
            if temp.next == None:
                temp.next = Node(value)
                break
            temp = temp.next

    def addOnBegin(self, value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp

    def addAfter(self, previous, data):
        if previous is None:
            return

        new_node = Node(data)
        new_node.next = previous.next
        previous.next = new_node

    def findInList(self, value):
        temp = self.head
        i = 0
        while temp:
            if temp.data == value:
                print(i)
                return temp
            temp = temp.next
            i += 1
        print(None)
        return None


l = LinkedList()
for x in range(1, 10):
    l.addOnEnd(x)

l.addOnBegin(0)
l.addAfter(l.findInList(3), 3)


l.printLinkedList()

# l.findInList(10) -> None
