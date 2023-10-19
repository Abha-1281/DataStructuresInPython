# Print top view of a Binary Tree
#
# Time Complexity: O(N), Since we only perform level-order traversal and print some
# part of the N nodes which at max will be 2N in case of skew tree
#
# Auxiliary Space: O(N), Since we store the nodes in
# the map and queue.

from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def topView(self, root, level, dic):
        if root is None:
            return
        q = [(root, level)]

        while q:
            node, level = q.pop(0)
            if level not in dic:
                dic[level] = node.data

            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))
        return dic


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)
    root.right.left = Node(90)
    root.right.right = Node(100)

    dic = defaultdict()
    dic = binaryTree.topView(root, 0, dic)
    for i in sorted(dic):
        print(dic[i])
