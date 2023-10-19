# Find The diameter/width of a tree . It is the number of nodes on the longest path between two end nodes.
# Time Complexity: O(N)
# Auxiliary Space: O(N) due to recursive calls.


# Solution is the find the maximum between the three following:

# The diameter of T’s left subtree.
# The diameter of T’s right subtree.
# The height of left Subtree + height of right subtree + 1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def findDiameter(self, root):
        if root is None:
            return (0, 0)  ##(diameter, height)

        leftDia, leftht = self.findDiameter(root.left)
        rightDia, rightht = self.findDiameter(root.right)

        currDia = max(max(leftDia, rightDia), leftht + rightht + 1)
        currht = max(leftht, rightht) + 1
        return (currDia, currht)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)
    dia, ht = binaryTree.findDiameter(root)
    print(dia)
