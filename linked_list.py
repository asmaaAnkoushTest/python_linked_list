
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

    def remove_at(self, index: int) -> int:
        removed: int
        if self.length <= index or index < 0:
            raise IndexError("Index Out Of Range")
        elif index == 0:
            removed = self.head.value
            self.head = self.head.next
            self.length -= 1
            return removed
        else:
            current: Node = self.head
            i: int = 0 
            while i < index - 1:
                prev = current
                current = current.next
                i += 1
            removed = current.next.value
            current.next = current.next.next
            self.length -= 1
            return removed
    
    def clear(self):
        self.head = None
        self.length = 0
