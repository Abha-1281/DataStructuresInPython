def maxSubArray(nums):
    sum = 0
    res = float('-inf')
    for i in nums:
        sum += i
        res = max(res, sum)
        if sum < 0:
            sum = 0
    return res


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
