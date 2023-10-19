# Given a binary tree, find if it is height balanced or not.
# A tree is height balanced if difference between heights of left and right subtrees is not more than one
# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.flag = 1

    def checkBalanced(self, root):
        if not root:
            return 0
        lh = self.checkBalanced(root.left)
        rh = self.checkBalanced(root.right)

        diff = abs(lh - rh)
        if diff > 1:
            self.flag = 0
        return 1 + max(lh, rh)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(5)
    root.left = Node(3)
    root.left.right = Node(4)

    binaryTree.checkBalanced(root)
    if binaryTree.flag == 0:
        print("Not Balanced")
    else:
        print("Balanced")
