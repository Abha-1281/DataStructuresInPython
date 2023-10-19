# Given a root of a BT , convert it into a BST

# Store the inorder of the BT in a list
# recursively pop the first element and change the root data

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.li = []

    def findInorder(self, root):
        if not root:
            return
        self.findInorder(root.left)
        self.li.append(root.data)
        self.findInorder(root.right)

    def convertToBst(self, root):
        if root is None:
            return
        self.convertToBst(root.left)
        root.data = self.li.pop(0)
        self.convertToBst(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    bst = BST()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    bst.findInorder(root)
    bst.li.sort()
    bst.convertToBst(root)
    bst.preorder(root)
