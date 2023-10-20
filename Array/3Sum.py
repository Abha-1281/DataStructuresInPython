# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# The solution is to find all the triplet whose sum is zero and the solution should not contain duplicate. loop
# through each distint elements and use two pointer technique



def threeSum( nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            if nums[i] + nums[j] + nums[k] < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return res

if __name__ == '__main__':
    nums = [-3,-3,1,1,2,3,4]
    print(threeSum(nums))
