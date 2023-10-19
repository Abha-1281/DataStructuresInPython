# Given two integer arrays preorder and inorder, construct and return the binary tree.
# TC: O(n)
# SC: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def buildTreeFromInorderPreorder(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTreeFromInorderPreorder(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTreeFromInorderPreorder(preorder[mid + 1:], inorder[mid + 1:])
        return root

    def preorder(self, root):
        if root is None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = binaryTree.buildTreeFromInorderPreorder(preorder, inorder)
    binaryTree.preorder(root)
