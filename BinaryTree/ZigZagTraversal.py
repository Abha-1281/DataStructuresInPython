# print zigzag traversal of a binary tree
# Time Complexity: O(N)
# Auxiliary Space: O(N) for deque data structure

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def zigZagTraversal(self, root, ans):
        flag = False
        q = [root]

        while q:
            res = []
            for i in range(len(q)):
                node = q.pop(0)
                res.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if flag:
                ans.extend(res[::-1])
            else:
                ans.extend(res)

            flag = not flag

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
    binaryTree.zigZagTraversal(root, ans)
    print(ans)
