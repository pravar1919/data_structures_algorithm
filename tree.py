class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    start with top node.
    if the next value is > that the root, will place to the right of that node.
    if the next value is < that of the root, will place to the left.
    this process continues.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:  # if the value is duplicate
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                # search left
                temp = temp.left
            elif value > temp.value:
                # search right
                temp = temp.right
            else:
                return True
        return False

            



b = BinaryTree()
b.insert(1)
b.insert(2)
b.insert(0)
b.insert(-1)
b.insert(-2)
b.insert(3)
print(b.root.value)
print(b.root.right.value)
print(b.root.left.value)
print(b.root.left.left.value)

print(b.contains(3))
