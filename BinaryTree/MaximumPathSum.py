# Find the maximum path sum in a binary tree

# We have to select a single path from a subtree root the left, and one to the right, and take the maximum possible
# answer considering all possible sums between them.

#
# Time complexity:
# O(n): We explore all nodes
# 
# Space complexity:
# O(1): Not considering recursion stack.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.res = root.data

    def maxPath(self, root):
        if root is None:
            return 0
        left = self.maxPath(root.left)
        right = self.maxPath(root.right)

        left = max(left, 0)
        right = max(right, 0)

        self.res = max(root.data + left + right, self.res)  #

        return root.data + max(left, right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    binaryTree = BinaryTree(root)
    binaryTree.maxPath(root)
    print(binaryTree.res)
