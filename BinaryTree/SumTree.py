# Given a Binary Tree of size N , where each node can have positive or negative values. Convert this to a tree where
# each node contains the sum of the left and right sub trees of the original tree. The values of leaf nodes are
# changed to 0.
#
# Time Complexity: O(n) where n is the number of nodes
# Auxiliary Space : O(1) since using constant variables

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def sumTree(self, root):
        if root is None:
            return 0
        left = self.sumTree(root.left)
        right = self.sumTree(root.right)

        oldValue = root.data
        root.data = left + right
        return oldValue + left + right

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    binaryTree = BinaryTree()
    binaryTree.sumTree(root)
    binaryTree.inorder(root)
