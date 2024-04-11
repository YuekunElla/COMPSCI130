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

def print_node_chain(first_node):
    current = first_node
    while current:
        print(f"Node({current})", end=" -> ")
        current = current.get_next()
    print("None")

def create_chain_nodes_from_list(a_list):
    current=Node(a_list[0])
    for i in range(len(a_list)-1):
        next_node=Node(a_list[i+1])
        current.set_next(next_node)
        current.add_after(Node(a_list[i]))
    return current
chain_nodes = create_chain_nodes_from_list([])
print_node_chain(chain_nodes)
