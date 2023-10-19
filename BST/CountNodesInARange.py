class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.ans = []

    def countNode(self, root, lb , ub):
        if root is None:
            return

        if root.data in range(lb, ub + 1):
            self.ans.append(root.data)
        self.countNode(root.left, lb, ub)
        self.countNode(root.right, lb, ub)
        return


if __name__ == '__main__':
    bst = BST()
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.right.left = Node(40)
    root.right.right = Node(100)

    bst.countNode(root, lb=4, ub=45)
    print(bst.ans)

