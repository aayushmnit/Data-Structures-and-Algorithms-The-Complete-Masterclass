class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items):
            return self.items.pop(0)
        
    def peek(self):
        if len(self.items) > 0:
            return self.items[0].value
    
    def __len__(self):
        return len(self.items)

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)

    def levelorder(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = []

        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left: queue.enqueue(node.left)
            if node.right: queue.enqueue(node.right)

        return traversal

    
        
tree = BinaryTree(3) ## Root

tree.root.left = Node(4) ## Root LEFT
tree.root.left.left = Node(6) ## Root Left left
tree.root.left.right = Node(7) ## Root Right right

tree.root.right = Node(5) ## Root Right
tree.root.right.left = Node(8) ## Root Right left
tree.root.right.right = Node(9) ## Root Right right

print(tree.levelorder(tree.root))