# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.


# Time complexity: O(m*n), worst case: for each node in the 1st tree, we need to check if isSameTree. Total m nodes,
# isSame(...) takes O(n) worst case Space complexity: O(height of 1str tree) or O(m) for worst case,
# O(logm) for average case)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def isSubTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubTree(root.left, subRoot.left) or self.isSubTree(root.right, subRoot.right)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        return root.data == subRoot.data and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right,
                                                                                                          subRoot.right)


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(2)

    subRoot = Node(4)
    subRoot.left = Node(1)
    subRoot.right = Node(2)

    binaryTree = BinaryTree()
    ans = binaryTree.isSubTree(root, subRoot)
    print(ans)
