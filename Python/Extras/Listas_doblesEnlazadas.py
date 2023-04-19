class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove_node(self, data):
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                
                return True
                
            current_node = current_node.next
        
        return False
    
    def search_node(self, data):
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == data:
                return current_node
            
            current_node = current_node.next
        
        return None
def print_list(list):
    current_node = list.head
    
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

my_list = DoublyLinkedList()
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(3)
my_list.add_node(3)
print_list(my_list)