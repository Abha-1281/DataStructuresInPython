# Print the Right View of a Binary tree

# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Auxiliary Space: O(N) since using auxiliary space for queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def rightView(self, root, ans):

        if root is None:
            return

        q = [root]

        while q:
            count = len(q)
            for i in range(len(q)):
                node = q.pop(0)
                if i == count - 1:
                    ans.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return ans


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
    ans = []
    binaryTree.rightView(root, ans)
    print(ans)
