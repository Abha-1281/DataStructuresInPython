# detect if the two trees are Isomorphic
# TC: The above solution does a traversal of both trees. So time complexity is O(min(m,n))
# Auxiliary Space: O(log min(n, m)), due to auxiliary stack space used by recursion calls.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def isIsomorphic(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 and not root2:
            return False
        if not root1 and root2:
            return False

        a = (root1.data == root2.data) and self.isIsomorphic(root1.left, root2.right) and self.isIsomorphic(root1.right,
                                                                                                            root2.left)
        b = (root1.data == root2.data) and self.isIsomorphic(root1.left, root2.left) and self.isIsomorphic(root1.right,
                                                                                                           root2.right)
        return a or b


if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)

    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)

    binaryTree = BinaryTree()
    print(binaryTree.isIsomorphic(root1, root2))
