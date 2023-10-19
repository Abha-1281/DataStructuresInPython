# Given a node , find the kth ancestor af that node in a binary tree. Return the kth ancestor data or -1 if the
# ancestor doesnot exist

# The solution is to first find the node and then backtrack until k<=0. Return -1 if the ancetor is None or if the
# node and the ancestor are equal
#
# Time Complexity: O(n), where n is the number of nodes in the binary tree. Auxiliary
# Space: O(h) where h is the height of binary tree due to recursion call.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def findKthAncestor(self, root, node, k):
        if root is None:
            return None
        if root.data == node:
            return root

        left = self.findKthAncestor(root.left, node, k)
        right = self.findKthAncestor(root.right, node, k)

        if left and not right:
            k[0] -= 1
            if k[0] <= 0:
                k[0] = float('inf')
                return root
            return left

        if right and not left:
            k[0] -= 1
            if k[0] <= 0:
                k[0] = float('inf')
                return root
            return right

        return None


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    binaryTree = BinaryTree()

    k = 2
    node = 4
    ans = binaryTree.findKthAncestor(root, node, [k])
    if ans is None or ans.data == node:
        print("-1")
    else:
        print(ans.data)
