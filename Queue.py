class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items.pop() 
    def size(self):
        return len(self.items)
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items[len(self.items)-1]
    def __str__(self):
        return '-> |' + str(self.items)[1:-1] + '| ->'
    def clear(self):
        self.items = []

