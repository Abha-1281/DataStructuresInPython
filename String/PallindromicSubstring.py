def countSubstrings( s):
    res = []
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res.append(s[l:r + 1])
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res.append(s[l:r + 1])
            l -= 1
            r += 1

    return len(res)


if __name__ == '__main__':
    s = "aaa"
    print(countSubstrings(s))  # Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
