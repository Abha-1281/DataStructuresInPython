# Find level order traversal of a Binary Tree

# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Auxiliary Space: O(N) where N is the number of nodes in the binary tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def levelOrderTraverse(self, root):
        if root is None:
            return

        q = [root]
        while q:
            node = q.pop(0)
            print(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)

    binaryTree.levelOrderTraverse(root)
