class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def deletion(self, root, key):
        if root is None:
            return
        if key < root.data:
            root.left = self.deletion(root.left, key)
        elif key > root.data:
            root.right = self.deletion(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                root.data = self.findSucc(root.right)
                root.right = self.deletion(root.right, root.data)

        return root

    def findSucc(self, root):
        if root.left:
            return self.findSucc(root.left)
        return root.data

    def preorder(self, root):
        if root is None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    bst = BST()
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(7)

    key = 3
    root = bst.deletion(root, 3)
    bst.preorder(root)
