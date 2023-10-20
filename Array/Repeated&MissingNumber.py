def repeated_Missing_Number(A):
    n = len(A)

    sumOfN = (n * (n + 1)) // 2
    sumOfDistictValues = sum(set(A))
    missingNum = sumOfN - sumOfDistictValues

    repeatedNum = sum(A) - sum(set(A))

    return [repeatedNum, missingNum]


if __name__ =='__main__':
    nums = [3 ,1 ,2 ,5,3]
    print(repeated_Missing_Number(nums))