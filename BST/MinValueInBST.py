class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def minValue(self, root):

        if root is None:
            return -1

        if root.left:
            return self.minValue(root.left)

        return root.data


if __name__ == '__main__':
    bst = BST()
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)

    print(bst.minValue(root))
