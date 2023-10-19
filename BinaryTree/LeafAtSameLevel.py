##Given a Binary Tree, check if all leaves are at same level or not.
# Time Complexity: The function does a simple traversal of the tree, so the complexity is O(n).
# Auxiliary Space: O(H) for call stack, where H is height of tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.leaflevel = None

    def atSameLevel(self, root, level):
        if root is None:
            return True

        if root.left is None and root.right is None:
            if self.leaflevel is None:
                self.leaflevel = level
                return True
            else:
                if self.leaflevel == level:
                    return True

            return False

        return self.atSameLevel(root.left, level + 1) and self.atSameLevel(root.right, level + 1)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)

    binaryTree = BinaryTree()
    level = 0
    print(binaryTree.atSameLevel(root, level))
