
def longestSubarray(arr, k):
    dic = {}
    sum = 0
    reslen = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            reslen = max(reslen, i + 1)

        diff = sum - k
        if diff in dic:
            reslen = max(reslen, i - dic[diff])

        if sum not in dic:
            dic[sum] = i

    return reslen


if __name__ == '__main__':
    nums = [10, 5, 2, 7, 1, 9]
    k = 15
    print(longestSubarray(nums, k))

