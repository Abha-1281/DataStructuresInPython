# Given an array of string . Write a function to find the longest common prefix string amongst all the strings in an
# array.


def longestCommonPrefix(strs):
    ans = ""
    sorted_strs = sorted(strs)
    first = sorted_strs[0]
    last = sorted_strs[-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
