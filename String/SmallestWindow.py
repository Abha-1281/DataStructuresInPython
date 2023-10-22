# Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.
# Return "-1" in case there is no such window present.


def smallestWindow( s, p):
    # code here
    if p == "":
        return ""

    reslen = float("inf")

    # what we need
    need = {}
    for i in p:
        need[i] = 1 + need.get(i, 0)
    needCount = len(need)

    have = {}
    haveCount = 0
    res = ""
    l = 0
    for r in range(len(s)):

        # have we have so far in each iteration
        have[s[r]] = 1 + have.get(s[r], 0)

        # update haveCount if we get the needed string
        if s[r] in need and have[s[r]] == need[s[r]]:
            haveCount += 1

        # if what we have is equal to what we needed, update the result and start sliding the window from left by
        # removing the left item from have map 

        while haveCount == needCount:
            if r - l + 1 < reslen:
                res = s[l:r + 1]
                reslen = r - l + 1


            have[s[l]] -= 1

            # update haveCount if we removed the needed string
            if s[l] in need and have[s[l]] < need[s[l]]:
                haveCount -= 1

            l += 1

    return res if reslen != float("inf") else -1


if __name__ == '__main__':
    s = "timetopractice"
    p = "toc"
    print(smallestWindow(s,p))
