# detect if the two trees are Same
# Time Complexity: O(min(N, M)), Where N and M are the sizes of the trees
# Auxiliary Space: O(log min(N, M)), due to auxiliary stack space used by recursion calls


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def isSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 and not root2:
            return False
        if not root1 and root2:
            return False

        return (root1.data == root2.data) and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right,
                                                                                                          root2.right)


if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)

    binaryTree = BinaryTree()
    print(binaryTree.isSameTree(root1, root2))
