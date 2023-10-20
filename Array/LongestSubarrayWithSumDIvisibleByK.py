# The subarray is {2,-5,12,-11,-1} with sum -3, which is divisible by 3.

def longSubarrWthSumDivByK(arr, n, k):
    dic = {}

    reslen = 0
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum % k == 0:
            reslen = max(reslen, i + 1)

        rem = sum % k
        if rem in dic:
            reslen = max(reslen, i - dic[rem])

        if sum % k not in dic:
            dic[sum % k] = i

    return reslen


if __name__ == '__main__':
    nums = [-2, 2, -5, 12, -11, -1, 7]
    k = 15
    print(
        longSubarrWthSumDivByK(nums, len(nums), k))  # The subarray is {2,-5,12,-11,-1} with sum -3,  is divisible by 3.
