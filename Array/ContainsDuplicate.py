def containsDuplicate(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in dic:
        if dic[i] > 1:
            return True
    return False


if __name__ == '__main__':
    arr = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(arr))
