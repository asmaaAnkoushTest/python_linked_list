
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, value):
        node: Node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def add(self, value):
        # Edge case
        node: Node = Node(value)
        if self.head is None:
            self.head = node 
        else:
            current: Node = self.head
            while current.next:
                current = current.next
            current.next = node
        self.length += 1

    def print_list(self):
        current: Node = self.head
        while current:
            print(f"{current.value} -> ", end = "")
            current = current.next
    
    def insert(self, index, value):
        node: Node = Node(value)
        if self.length < index or index < 0:
            raise IndexError("Index Out Of Range")
        elif index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            current: Node = self.head
            i: int = 0 
            while i < index - 1:
                current = current.next
                i += 1
            node.next = current.next
            current.next = node
            self.length += 1



    
# ll = LinkedList()
# ll.append(10)
# ll.append(5)
# ll.insert(2, 15)
# ll.insert(2,20)

# print(ll.length)
# ll.print_list()