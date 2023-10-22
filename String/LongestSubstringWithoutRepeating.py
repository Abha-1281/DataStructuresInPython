def lengthOfLongestSubstring(s):
    maxlen = 0
    lookup = set()
    l = 0
    r = 0
    while r < len(s):
        while s[r] in lookup:
            lookup.remove(s[l])
            l += 1
        lookup.add(s[r])
        maxlen = max(maxlen, r - l + 1)
        r += 1

    return maxlen


if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
