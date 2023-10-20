def trappingRain(height) -> int:
    l = 0
    r = len(height) - 1
    leftmax = height[l]
    rightmax = height[r]

    res = 0
    while l < r:
        if leftmax < rightmax:
            l += 1
            leftmax = max(leftmax, height[l])
            res += leftmax - height[l]
        else:
            r -= 1
            rightmax = max(rightmax, height[r])
            res += rightmax - height[r]

    return res


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trappingRain(height))
