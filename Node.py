class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)

class LinkedList:   
    def __init__(self):
        self.head = None
        self.count = 0

    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count =0 
            
    def is_empty(self):
        return self.head == None
        
    def __str__(self):
        if self.is_empty():
            return ""
        result = 'Head: '
        current = self.head
        while current:
            result += str(current.data) + ' --> '
            current = current.next
        return result[:-4]
    
    
values = LinkedList()
values.add("hello")
values.add("world")
print(values)
values.clear()
print(values)
print(values.size())



















        

    
