class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def checkDeadEnd(self, root, mini, maxa):
        if root is None:
            return False

        if mini == maxa:
            return True

        return self.checkDeadEnd(root.left, mini, root.data - 1) or self.checkDeadEnd(root.right, root.data + 1, maxa)


if __name__ == '__main__':
    bst = BST()
    root = Node(8)
    root.left = Node(1)
    root.right = Node(9)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.left.left.left = Node(1)

    print(bst.checkDeadEnd(root, 1, float('inf')))
