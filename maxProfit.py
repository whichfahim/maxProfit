def maxProfit(prices):
    if len(prices)<2:
        return 0
    else:
        # buy = 999
        sell = 0
        profit = 0

        for i in range(1,len(prices)):
            # if prices[i]>=sell:
            sell = prices[i]
            buy = min(prices[:i])
            profit = max(profit, sell-buy)

    
    if profit>0:
        return profit
    else:
        return 0

print(maxProfit(prices = [10,1,5,6,7,1]))

# Output: 6


print(maxProfit(prices = [10,8,7,5,2]))
# Output: 0

print(maxProfit(prices=[3,2,6,5,0,3]))
# Output: 4


print(maxProfit(prices=[5,1,5,6,7,1,10]))
# Output: 9

print(maxProfit(prices=[2,1,2,1,0,1,2]))
# Output: 2

print(maxProfit(prices=[3,3,5,0,0,3,1,4]))
# Output: 4
