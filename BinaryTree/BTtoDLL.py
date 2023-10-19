# Convert a Binary Tree to  Doubly linked list

# Time Complexity: O(n)
# Auxiliary Space: O(h)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeToDLL:

    def __init__(self):
        self.flag = 0
        self.prev = None
        self.head = None

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        if self.flag == 0:
            self.flag = 1
            self.prev = root
            self.head = root

        else:
            self.prev.right = root
            self.prev.right.left = self.prev
            self.prev = self.prev.right

        self.inorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    #   1
    #  /  \
    # 2    3

    binaryTreeToDll = BinaryTreeToDLL()
    binaryTreeToDll.inorder(root)
    print(binaryTreeToDll.head.data)
