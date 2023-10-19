# Given an array which represent a Binary Tree. FInd the min number of swaps required to comvert it into a BST


# The idea is to use the fact that inorder traversal of Binary Search Tree is in increasing order of their value. So,
# find the inorder traversal of the Binary Tree and store it in the array and try to sort the array. The minimum
# number of swap required to get the array sorted will be the answer.

# Time Complexity: O(n*logn)
# Auxiliary Space: O(n) because it is using extra space for array


def inorder(arr, i, res):
    if i < len(arr):
        inorder(arr, 2 * i + 1, res)
        res.append(arr[i])
        inorder(arr, 2 * i + 2, res)
    return res


def findMinSwap(res):
    nums = [[res[i], i] for i in range(len(res))]
    nums.sort()
    count = 0

    for i in range(len(res)):
        if nums[i][1] == i:
            continue
        while nums[i][1] != i:
            y = nums[i][1]
            nums[i], nums[y] = nums[y], nums[i]
            count += 1

    return count


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 10, 11];
    res = []
    res = inorder(arr, 0, res)
    print(findMinSwap(res))
