class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(root, inorder):
    if not inorder:
        return None
    mid = len(inorder) // 2
    root = Node(inorder[mid])
    root.left = buildTree(root.left, inorder[:mid])
    root.right = buildTree(root.right, inorder[mid + 1:])
    return root


def printInorder( root):
    if root is None:
        print("null")
        return

    printInorder(root.left)
    print(root.data)
    printInorder(root.right)


if __name__ == '__main__':
    post = [1, 7, 5, 50, 40, 10]
    root = None
    root = buildTree(root, inorder=sorted(post))
    printInorder(root)
