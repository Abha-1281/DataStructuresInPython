def findSum( A):
    # code here

    mini = A[0]
    maxi = A[0]

    for i in A:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i

    return mini + maxi


if __name__ == '__main__':
    A = [-2, 1, -4, 5, 3]
    print(findSum(A))
