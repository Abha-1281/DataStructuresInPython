# Given a binary tree, find out whether it contains a duplicate sub-tree of size two or more, or not.
# (exclude leaf node)


# The solution is to traverse the Binary tree and keep a record of the string pattern of nodes encountered and store
# in a dictionary. If dic contains a pattern more than once we found a duplicate
# TC: O(n) SC: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.dic = {}

    def duplicateSubtreeExist(self, root):
        if root is None:
            return "null"

        # size of leaf node is one so exclude from the solution
        if not root.left and not root.right:
            return str(root.data)
        
        l = self.duplicateSubtreeExist(root.left)
        r = self.duplicateSubtreeExist(root.right)
        s = str(root.data) + "," + l + "," + r
        if s not in self.dic:
            self.dic[s] = 1
        else:
            self.dic[s] += 1

        return s


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.right = Node(2)
    root.right.right.left = Node(4)
    root.right.right.right = Node(5)

    s = binaryTree.duplicateSubtreeExist(root)
    exist = None
    for i in binaryTree.dic:
        if binaryTree.dic[i] > 1:
            exist = True
            break
        else:
            exist = False

    if exist:
        print("Duplicate subtree Exist")
    else:
        print("Duplicate subtree does not exist")
