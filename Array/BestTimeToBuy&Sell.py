def findMaxProfit(prices):
    minCostPrice = float('inf')
    maxProfit = 0

    for i in range(len(prices)):
        minCostPrice = min(minCostPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - minCostPrice)

    return maxProfit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(findMaxProfit(prices))

