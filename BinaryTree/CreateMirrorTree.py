# Given a binary tree, the task is to create a new binary tree which is a mirror image of the given binary tree.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Auxiliary Space: O(h), where h is the height of the binary tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def createMirrorTree(self, root, mirrorTree):
        if root is None:
            return None
        mirrorTree = Node(root.data)
        mirrorTree.left = self.createMirrorTree(root.right, mirrorTree.left)
        mirrorTree.right = self.createMirrorTree(root.left, mirrorTree.right)
        return mirrorTree

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)

    mirrorTree = None
    mirrorTree = binaryTree.createMirrorTree(root, mirrorTree)
    binaryTree.inorder(mirrorTree)
