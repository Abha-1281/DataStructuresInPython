# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have
# a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:

# Each student gets one packet.
#
# The difference between the number of chocolates in the packet with maximum chocolates
# and the packet with minimum chocolates given to the students is minimum.

def findMinDiff(A, N, M):
    res = float('inf')
    # code here
    A.sort()

    for i in range(N - M + 1):
        j = i + M - 1
        res = min(res, A[j] - A[i])
        j += 1

    return res


if __name__ == '__main__':
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    N = 8
    M = 5
    print(findMinDiff(arr, N, M))
