
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


    
# ll = LinkedList()
# ll.append(10)
# ll.append(5)
# ll.add(20)

# print(ll.length)
# ll.print_list()