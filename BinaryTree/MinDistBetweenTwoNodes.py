# Find the Minimum distance between two nodes in a binary tree

# First find the lca of the two nodes . then find the distance from lca to each of the nodes and add the two distance

# Time Complexity: O(n), As the method does a single tree traversal. Here n is the number of elements in the tree.
# Auxiliary Space: O(h), Here h is the height of the tree and the extra space is used in

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def lca(self, root, n1, n2):

        if root is None:
            return None

        if root.data == n1 or root.data == n2:
            return root

        l = self.lca(root.left, n1, n2)
        r = self.lca(root.right, n1, n2)

        if l and r:
            return root
        if l:
            return l
        else:
            return r

    def findDist(self, root, n, level):
        if root is None:
            return 0
        if root.data == n:
            return level
        l = self.findDist(root.left, n, level + 1)
        r = self.findDist(root.right, n, level + 1)
        return max(l, r)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    n1 = 2
    n2 = 3
    l = binaryTree.lca(root, n1, n2)
    d1 = binaryTree.findDist(l, n1, 0)
    d2 = binaryTree.findDist(l, n2, 0)
    print(d1 + d2)
