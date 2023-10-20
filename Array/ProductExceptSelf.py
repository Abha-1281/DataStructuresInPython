# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].


def productExceptSelf(nums):
    n = len(nums)
    temp1 = [1] * n
    temp2 = [1] * n

    res = [1] * n

    for i in range(1, n):
        temp1[i] = temp1[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        temp2[i] = temp2[i + 1] * nums[i + 1]

    for i in range(n):
        res[i] = temp1[i] * temp2[i]

    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
