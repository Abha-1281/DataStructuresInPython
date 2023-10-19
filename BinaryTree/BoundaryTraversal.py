# Print boundary nodes of a binary tree

# Solution is to traverse left boundary excluding leaf + traverse left subtree leaf nodes + traverse right subtree
# leaf nodes+ right boundary in post order
# Time Complexity: O(n) where n is the number of nodes in binary tree.
# Auxiliary Space: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.ans = []

    def leftBoundary(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        self.ans.append(root.data)
        if root.left:
            self.leftBoundary(root.left)
        else:
            self.leftBoundary(root.right)

    def rightBoundary(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return

        if root.right:
            self.rightBoundary(root.right)
        else:
            self.rightBoundary(root.left)
        self.ans.append(root.data)

    def leafNodes(self, root):
        if root is None:
            return
        if not root.left and not root.right:
            self.ans.append(root.data)
            return
        self.leafNodes(root.left)
        self.leafNodes(root.right)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)

    binaryTree.ans = [root.data]
    binaryTree.leftBoundary(root.left)
    binaryTree.leafNodes(root.left)
    binaryTree.leafNodes(root.right)
    binaryTree.rightBoundary(root.right)

    print(binaryTree.ans)
