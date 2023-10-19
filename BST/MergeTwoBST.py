# Given Two BST , Merge the two bst and return the elements of both the bst in a sorted form in an array

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, li):
    if root is None:
        return
    inorder(root.left, li)
    li.append(root.data)
    inorder(root.right, li)


def mergeSortedList(arr1, arr2, ans):
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1


if __name__ == '__main__':
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(6)
    root1.left.left = Node(2)
    root1.left.right = Node(4)


    root2 = Node(2)
    root2.left = Node(1)
    root2.right = Node(3)
    root2.right.right = Node(7)
    root2.right.right.left = Node(6)

    li1 = []
    li2 = []
    inorder(root1,li1)
    inorder(root2, li2)

    ans = []
    mergeSortedList(li1,li2, ans)
    print(ans)
