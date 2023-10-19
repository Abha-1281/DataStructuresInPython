# Find the number of paths in the tree which have their sum equal to K.

# Solution is to keep the track of the prefix sum in a dictionary
# TC: O(n)
# SC: O(H)


from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.count = 0

    def findKSumPath(self, root, sum, k, dic):
        if root is None:
            return 0

        sum += root.data

        if sum - k in dic:
            self.count += dic[sum - k]

        if sum == k:
            self.count += 1

        dic[sum] += 1
        self.findKSumPath(root.left, sum, k, dic)
        self.findKSumPath(root.right, sum, k, dic)
        dic[sum] -= 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    #   1
    #  /  \
    # 2    3

    binaryTree = BinaryTree()
    sum = 0
    dic = defaultdict(int)
    k = 3
    binaryTree.findKSumPath(root, sum, k, dic)
    print(binaryTree.count)
