class BST:
    class BSTNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self.root = root

    def search_subtree(self, root, key):
        if root is None:
            return None
        if key == root.data:
            return root
        if key < root.data:
            return self.search_subtree(root.left, key)
        return self.search_subtree(root.right, key)

    def insert(self, root, key):
        if root is None:
            return BST.BSTNode(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def delete_subtree(self, root, key):
        if root is None:
            return None
        if root.data == key:
            return None
        if key < root.data:
            root.left = self.delete_subtree(root.left, key)
        else:
            root.right = self.delete_subtree(root.right, key)
        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.data))
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = 1

    def __init__(self, root=None):
        self.root = root

    def get_height(self, node):
        return 0 if node is None else node.height

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def _rebalance(self, node):
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def insert(self, root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root = self.update_height(root)
        return self._rebalance(root)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.data] + self.inorder_traversal(root.right)

    def _build_balanced_from_sorted(self, arr, l, r):
        if l > r:
            return None
        m = (l + r) // 2
        node = AVLTree.AVLNode(arr[m])
        node.left = self._build_balanced_from_sorted(arr, l, m - 1)
        node.right = self._build_balanced_from_sorted(arr, m + 1, r)
        return self.update_height(node)

    def bst_to_avl(self, bst_root):
        vals = self.inorder_traversal(bst_root)
        self.root = self._build_balanced_from_sorted(vals, 0, len(vals) - 1)

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.data))
            self.printTree90(root.left, indent + 1)


inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for x in inp1.split():
    bst.root = bst.insert(bst.root, int(x))

print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
if subtree_root:
    avl1.bst_to_avl(subtree_root)
    avl1.printTree90(avl1.root)

print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
if bst.root:
    avl2.bst_to_avl(bst.root)
    avl2.printTree90(avl2.root)
