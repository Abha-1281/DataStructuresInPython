# Set the next pointer of each node to point to the inorder successor.

# Solution is to store the inorder in the tree in a list and then iterate through the list to point the next ptr of
# each node to the next i+1 element in the list

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


class BST:

    def getinorder(self, root, li):
        if root is None:
            return
        self.getinorder(root.left, li)
        li.append(root)
        self.getinorder(root.right, li)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.data)
        if root.next:
            print("next", root.next.data)
        else:
            print("NULL")

        self.inorder(root.right)


if __name__ == '__main__':
    bst = BST()
    root = Node(10)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(3)

    li = []
    bst.getinorder(root, li)
    for i in range(len(li) - 1):
        li[i].next = li[i + 1]

    bst.inorder(root)
