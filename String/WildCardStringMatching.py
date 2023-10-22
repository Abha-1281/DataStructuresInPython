
def stringMatch(strs, pattern, i, j):
    if i < 0 and j < 0:
        return True
    if i >= 0 and j < 0:
        return False
    if i < 0 and j >= 0:
        for jj in range(j):
            if pattern[jj] != "*":
                return False
        return True
    else:
        if strs[i] == pattern[j] or pattern[j] == "?":
            return stringMatch(strs, pattern, i - 1, j - 1)
        elif pattern[j] == "*":
            return stringMatch(strs, pattern, i - 1, j) or stringMatch(strs, pattern, i, j - 1)
        else:
            return False


if __name__ == '__main__':
    strs = "geeksforgeeks"
    pattern = "ge?ks*"
    print(stringMatch(strs, pattern, len(strs)-1, len(pattern)-1))
