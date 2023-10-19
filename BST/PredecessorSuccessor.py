# In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than
# the target is the successor.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def findSucc(self, root, key, succ):
        if root is None:
            return
        if root.data > key:
            succ[0] = root.data
            self.findSucc(root.left, key, succ)
        else:
            self.findSucc(root.right, key, succ)
        return

    def findPred(self, root, key, pred):
        if root is None:
            return
        if root.data < key:
            pred[0] = root.data
            self.findPred(root.right, key, pred)
        else:
            self.findPred(root.left, key, pred)
        return


if __name__ == '__main__':
    bst = BST()
    root = Node(8)
    root.left = Node(1)
    root.right = Node(9)
    root.left.right = Node(4)
    root.right.right = Node(10)
    root.left.right.left = Node(3)

    succ = [-1]
    pred = [-1]
    key = 11
    bst.findSucc(root, key, succ)
    bst.findPred(root, key, pred)

    print(pred[0])
    print(succ[0])
