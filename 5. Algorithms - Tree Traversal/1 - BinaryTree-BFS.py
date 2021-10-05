






class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)


tree = BinaryTree(3) ## Root

tree.root.left = Node(4) ## Root LEFT
tree.root.left.left = Node(6) ## Root Left left
tree.root.left.right = Node(7) ## Root Right right

tree.root.right = Node(5) ## Root Right
tree.root.right.left = Node(8) ## Root Right left
tree.root.right.right = Node(9) ## Root Right right