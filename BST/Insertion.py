#Insert a node in a BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def insert(self, root, Key):
        # code here

        if not root:
            return Node(Key)
        if Key < root.data:
            root.left = self.insert(root.left, Key)
        elif Key > root.data:
            root.right = self.insert(root.right, Key)
        return root


if __name__ == '__main__':
    bst = BinarySearchTree()
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)

    key = 40
    root = bst.insert(root, key)
    print(root.right.right.data)