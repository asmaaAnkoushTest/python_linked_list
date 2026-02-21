
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
        print("None")
    
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

    def contains(self,value) -> bool:
        current: Node = self.head
        if self.length == 0:
            return False
        else:
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False
        
    def index_of(self, value) -> int:
        current: Node = self.head
        index: int = 0
        if self.length == 0:
            return -1
        else:
            while current:
                if current.value == value:
                    return index
                index += 1
                current = current.next
            return -1
        
    def for_each(self, action):
        current: Node = self.head
        while current:
            current.value = (action)(current.value)
            current = current.next
    
    def map(self, action) -> LinkedList:
        current: Node = self.head
        new_list: LinkedList = LinkedList()
        while current:
            new_value = (action)(current.value)
            new_list.add(new_value)
            current = current.next
        return new_list

    def where (self, action) -> LinkedList:
        current: Node = self.head
        new_list: LinkedList = LinkedList()
        while current:
            if (action)(current.value) is True:
                new_list.add(current.value)
            else:
                pass
            current = current.next
        return new_list
    
    def __str__(self):
        current: Node = self.head
        string: str = ""
        while current:
            string = string + f"{current.value} -> "
            current = current.next
        string = string + "None"
        return string
