# Find the kth largest element in a BST

# The solution is to do a RNL traversal( Right, Node, Left) and keep increment the counter until k is reached

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.count = 0
        self.ans = -1

    def reverseInorder(self, root, k):
        if root is None:
            return
        self.reverseInorder(root.right, k)
        self.count += 1
        if self.count == k:
            self.ans = root.data
            return
        self.reverseInorder(root.left, k)
        return


if __name__ == '__main__':
    bst = BST()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(9)

    k = 2
    bst.reverseInorder(root, k)
    print(bst.ans)
