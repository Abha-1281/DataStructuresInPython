# Convert normal BS to a Balanced BST

# Solution is to find the inorder of the bst and store in an array
# find the mid node in the arr and recursively call the left subarray and right subarray to construct the balanced BST


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def findInorder(self, root, li):
        if root is None:
            return
        self.findInorder(root.left, li)
        li.append(root.data)
        self.findInorder(root.right, li)

    def createBalanceedBST(self, nums, root):
        if len(nums) == 0:
            return None
        l = 0
        u = len(nums) - 1
        mid = (u - l) // 2
        root = Node(nums[mid])
        root.left = self.createBalanceedBST(nums[:mid], root)
        root.right = self.createBalanceedBST(nums[mid + 1:], root)
        return root

    def printInorder(self, root):
        if root is None:
            print("null")
            return

        self.printInorder(root.left)
        print(root.data)
        self.printInorder(root.right)


if __name__ == '__main__':
    bst = BST()
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)

    li = []
    bst.findInorder(root, li)

    balancedBTS = None
    balancedBTS = bst.createBalanceedBST(li, balancedBTS)
    bst.printInorder(balancedBTS)
