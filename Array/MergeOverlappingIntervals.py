def overlappedInterval(intervals):
    # Code here
    intervals.sort()
    ans = []
    ans.append(intervals[0])

    for nextInterval in intervals[1:]:
        if ans[-1][1] >= nextInterval[0]:
            ans[-1][1] = max(ans[-1][1], nextInterval[1])
        else:
            ans.append(nextInterval)

    return ans


if __name__ == '__main__':
    intervals = [[6, 8], [2, 4], [1, 3], [9, 10]]
    print(overlappedInterval(intervals))
