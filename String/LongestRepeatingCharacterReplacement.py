def characterReplacement(s, k):
    l = 0
    r = 0
    dic = {}
    reslen = 0
    while r < len(s):
        if s[r] not in dic:
            dic[s[r]] = 1
        else:
            dic[s[r]] += 1

        window = r - l + 1
        maxrepeat = max(dic.values())
        nonrepeat = window - maxrepeat
        if nonrepeat > k:
            dic[s[l]] -= 1
            l += 1
        reslen = max(reslen, r - l + 1)
        r += 1

    return reslen


if __name__ == '__main__':
    s = "ABAB"
    k = 2
    print(characterReplacement(s, k))
