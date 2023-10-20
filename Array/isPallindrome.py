# Given a Integer array of n elements. Check if all the elements are palindrome. Return 1 if all are pallindrome
# otherwise 0


def PalinArray(arr, n):
    for i in arr:
        if not isPallindrome(str(i)):
            return 0
    return 1


def isPallindrome(val):
    return val == val[::-1]


if __name__ == '__main__':
    n = 5
    nums = [111, 222, 333, 444, 555]
    print(PalinArray(nums, n))
