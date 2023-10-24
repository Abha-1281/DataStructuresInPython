# Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.


# The solution is to keep the track of distinct elements in a dictionary. slide the window by removing elements from
# the left and adding elements from the right


def countDistinct(A, N, K):
    # Code here
    res = []
    dic = {}
    for i in range(k):
        dic[arr[i]] = 1 + dic.get(arr[i], 0)

    res.append(len(dic))

    for i in range(K, N):
        if dic[arr[i - K]] == 1:
            del dic[arr[i - K]]
        else:
            dic[arr[i - K]] -= 1

        dic[arr[i]] = 1 + dic.get(arr[i], 0)
        res.append(len(dic))

    return res



if __name__ == '__main__':
    arr = [1,2,1,3,4,2,3]
    k = 4
    print(countDistinct(arr, len(arr),k))