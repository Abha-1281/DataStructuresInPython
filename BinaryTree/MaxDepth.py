# Find Maximum depth or height of a binary tree

# TC - O(num of nodes) as we are traversing all the nodes of the tree
# SC - O(height of the tree) for the recursive stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    binaryTree = BinaryTree()
    depth = binaryTree.maxDepth(root)
    print(depth)
