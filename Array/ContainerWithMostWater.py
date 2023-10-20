
def maxArea(height):
    l = 0
    r = len(height) - 1
    res = 0

    while l < r:
        if height[l] < height[r]:
            currentWaterAmount = (r - l) * height[l]
            l += 1
        else:
            currentWaterAmount = (r - l) * height[r]
            r -= 1

        res = max(res, currentWaterAmount)

    return res


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))
