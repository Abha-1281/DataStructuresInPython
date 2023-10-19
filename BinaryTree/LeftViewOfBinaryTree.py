# Print left view of a Binary Tree
# Time Complexity: O(N), where n is the number of nodes in the binary tree.
# Auxiliary Space: O(N) since using space for auxiliary queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def leftview(self, root):
        if root is None:
            return

        q = [root]
        while q:
            # loop through all the nodes in the current queue level
            count = 0
            for i in range(len(q)):
                node = q.pop(0)
                if count == 0:
                    print(node.data)
                    count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.right = Node(8)

    binaryTree = BinaryTree()
    binaryTree.leftview(root)
