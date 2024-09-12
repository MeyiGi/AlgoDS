class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def append(self, data):
        new_node = Node(data)
        self.length += 1
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def print_list(self):
        current = linkedlist.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        else:
            print(None)
            
    def insert_center(self, data):
        slow = self.head
        fast = self.head.next
        
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        node = Node(data)
        node.next = slow.next
        
        slow.next = node
    
    def pop(self):
        if self.head is None:
            raise IndexError("Impossible to pop empty list")
        
        current = self.head
        
        while current.next.next:
            current = current.next
        
        value = current.next.val
        current.next = None
        
        return value
            
            
linkedlist = LinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(7)


linkedlist.print_list()

linkedlist.insert_center(100)
linkedlist.print_list()

print(linkedlist.pop())
linkedlist.print_list()
print(linkedlist.length)