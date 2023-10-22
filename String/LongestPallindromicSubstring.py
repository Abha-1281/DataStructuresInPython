def longestPalindrome(s):
    n = len(s)
    reslen = 0
    res = ""

    for i in range(n):
        l = i
        r = i

        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > reslen:
                reslen = r - l + 1
                res = s[l:r + 1]
            l -= 1
            r += 1

        l = i
        r = i + 1

        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > reslen:
                reslen = r - l + 1
                res = s[l:r + 1]
            l -= 1
            r += 1

    return res


if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(s))
