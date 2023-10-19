# Insert a node in a binary tree using recursion

# TC - height of the tree , Worst case: O(n)
# SC - O(height of the tree) for the recursive stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    def preorder(self, root):
        if root is None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    root = None
    binaryTree = BinaryTree()
    root = binaryTree.insert(root, 10)
    root = binaryTree.insert(root, 20)
    root = binaryTree.insert(root, 30)
    root = binaryTree.insert(root, 40)
    binaryTree.preorder(root)
