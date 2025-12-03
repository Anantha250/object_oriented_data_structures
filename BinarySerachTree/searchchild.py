class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        while True:
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(data)
                    break
                node = node.right

    def search_val(self, node, val):
        while node is not None:
            if val == node.data:
                return node
            elif val < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def search_child(self, node):
        if node is None:
            return []
        return [node.data] + self.search_child(node.left) + self.search_child(node.right)
        
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()

inp = [i for i in input("Enter the BST values and search value: ").split(", ")]

bst_inp = [int(i) for i in inp[0].split()]
print(f"Input: root = {bst_inp}, val = {inp[1]}")

for i in bst_inp:
    root = T.insert(i)

new_root = T.search_val(root, int(inp[1]))
print("Output:", T.search_child(new_root))
