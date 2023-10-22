def sameChar(A, B):
    # code here
    ans = 0
    for i in range(len(A)):
        if A[i].lower() == B[i].lower():
            ans += 1

    return ans


if __name__ == '__main__':
    A = "choice"
    B = "chancE"
    print(sameChar(A, B))
