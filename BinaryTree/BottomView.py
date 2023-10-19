# Print the Bottom view of a Binary Tree
# TC: O(n)
# SC: O(n)


from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def bottomView(self, root, level, dic):
        if root is None:
            return
        q = [(root, level)]

        while q:
            node, level = q.pop(0)
            dic[level] = node.data

            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))
        return dic


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    dic = defaultdict()
    dic = binaryTree.bottomView(root, 0, dic)
    for i in sorted(dic):
        print(dic[i])
