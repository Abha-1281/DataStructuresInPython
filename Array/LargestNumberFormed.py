
if __name__ == '__main__':
    arr = [3, 30, 34, 5, 9]
    arr = [str(i) for i in arr]
    arr.sort(key=lambda s: s * 7, reverse=True)
    ans = "".join(arr)
    print(ans)
