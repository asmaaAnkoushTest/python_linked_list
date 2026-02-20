
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add(self, value):
        # Edge case
        node: Node = Node(value)
        if self.head is None:
            self.head = node 
        else :
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


    
# print("##HIII##")
# ll = LinkedList()
# ll.add(10)

# print(ll.length)
# ll.print_list()