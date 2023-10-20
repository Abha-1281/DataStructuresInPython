# FInd minimum in a rotated sorted array

def findMin(nums):
    l = 0
    u = len(nums) - 1
    while l < u:
        mid = l + (u - l) // 2
        if nums[l] <= nums[mid] and nums[mid] > nums[u]:
            l = mid + 1
        else:
            u = mid

    return nums[l]


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(findMin(nums))
