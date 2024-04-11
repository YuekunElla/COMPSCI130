class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

def count_multiple_of_3(my_tree):
    if my_tree == None:
        return 0
    else:
        count=0
        current_data = my_tree.get_data()
        if current_data % 3 ==0:
            count += 1
        current_data = count_multiple_of_3(my_tree.get_left())
        current_data = count_multiple_of_3(my_tree.get_right())
        return count

print(count_multiple_of_3(BinaryTree(21, BinaryTree(20, BinaryTree(9), BinaryTree(9)), BinaryTree(65, BinaryTree(50), BinaryTree(91)))))
