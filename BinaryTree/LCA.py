# Find the lowest common Ancestor of a binary tree
# Time Complexity: O(N) as the method does a simple tree traversal in a bottom-up fashion.
# Auxiliary Space: O(H), where h is the height of the tree.

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


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(5)
    root.left = Node(2)

    root.left.left = Node(3)
    root.left.right = Node(4)
    node = binaryTree.lca(root, 3, 4)
    print(node.data)
