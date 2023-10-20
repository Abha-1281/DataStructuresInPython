def nextPermutation(nums):
    i = len(nums) - 2
    j = len(nums) - 1

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    while i >= 0 and j > i and nums[j] <= nums[i]:
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = reversed(nums[i + 1:])


if __name__ == '__main__':
    nums = [1, 1, 5]
    nextPermutation(nums)
    print(nums)
