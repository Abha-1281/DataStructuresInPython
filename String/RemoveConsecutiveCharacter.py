def removeConsecutiveCharacter( S):
    # code here
    ans = []
    for i in range(len(S)):
        if i > 0 and S[i - 1] == S[i]:
            continue
        ans.append(S[i])
    return "".join(ans)


if __name__  == '__main__':
    S = "aabb"
    print(removeConsecutiveCharacter(S))