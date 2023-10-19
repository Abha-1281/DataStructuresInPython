# Print the Diagonal Traversal of a Binary Tree
# TC: O(n)
# SC: O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def bottomView(self, root, ans):
        if root is None:
            return ans
        q = [root]
        while q:
            node = q.pop(0)
            while node:
                ans.append(node.data)
                if node.left:
                    q.append(node.left)
                node = node.right

        return ans


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right.left = Node(13)

    ans = []
    binaryTree.bottomView(root, ans)
    print(ans)
