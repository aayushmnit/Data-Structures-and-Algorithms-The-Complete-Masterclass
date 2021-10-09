class Node():
    def __init__(self, value):
        self.value = value
        self.adjacent_list = []
        self.visited = False

class Queue():
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
    
    def peek(self):
        if len(self.items) > 0:
            return self.items(0).value

class Graph():
    
    def BFS(self, node):
        queue = Queue()
        queue.enqueue(node)
        node.visited = True

        traversal = []

        while len(queue) > 0:
            actualNode = queue.dequeue()
            traversal.append(actualNode.value)

            for element in actualNode.adjacent_list:
                if element.visited is False:
                    queue.enqueue(element)
                    element.visited = True

        return traversal

    def DFS(self, node, traversal):
        node.visited = True
        traversal.append(node.value)
        for element in node.adjacent_list:
            if element.visited is False:
                self.DFS(element, traversal)

        return traversal

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')
node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node1.adjacent_list.append(node4)
node2.adjacent_list.append(node5)
node2.adjacent_list.append(node6)
node4.adjacent_list.append(node7)

print('BFS Traversal: \n',Graph().BFS(node1))

for node in [node1, node2, node3, node4, node5, node6, node7]:
    node.visited = False
    
print('DFS Traversal: \n',Graph().DFS(node1, []))