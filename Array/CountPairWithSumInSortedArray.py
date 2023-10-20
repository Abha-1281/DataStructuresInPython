# Find the number of pair in a sorted array whose sum is equal to the given sum. Return -1 if no such pair exist

# Solution is to use two pointer technique with left and right pointer


def Countpair(arr, n, sum):
    # Complete the function

    l = 0
    r = n - 1
    count = 0
    while l < r:
        if arr[l] + arr[r] > sum:
            r -= 1
        elif arr[l] + arr[r] < sum:
            l += 1
        else:
            count += 1
            l += 1
            r -= 1

    if count == 0:
        return -1
    else:
        return count


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    sum = 8
    print(Countpair(nums, len(nums), sum))  ## We find 3 such pairs that sum to 8 (1,7) (2,6) (3,5)
