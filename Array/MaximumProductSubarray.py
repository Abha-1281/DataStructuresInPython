# Given an array with negative numbers, find the subarray with maximum product

# The solution is to find the maximum between the prefix product and suffix product.

def maxProduct(nums):
    n = len(nums)
    pre = 1
    suf = 1
    res = float('-inf')
    for i in range(n):

        if pre == 0:
            pre = 1
        if suf == 0:
            suf = 1

        pre = pre * nums[i]
        suf = suf * nums[n - i - 1]
        res = max(res, max(pre, suf))

    return res


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print(maxProduct(nums))
