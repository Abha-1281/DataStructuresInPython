class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if root is None:
            return None

        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.prev
        self.prev = root

    def preorder(self, root):
        if root is None:
            print("null")
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    bst = BST()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)

    bst.flatten(root)
    bst.preorder(bst.prev)

