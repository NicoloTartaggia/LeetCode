class Solution:
    def maxProfit(self, prices):
        profit = 0
        #for i in range(len(prices)):
        #    for j in range(i+1, len(prices)):
        #        curr_profit = prices[j] - prices[i]
        #        if curr_profit > profit:
        #            profit = curr_profit
        i, j = 0, len(prices)-1
        while j > i:
            curr_profit = prices[j] - prices[i]
            if curr_profit > profit:
                profit = curr_profit 
            if prices[j] > prices[i]:
                j -= 1
            else:
                i += 1
        return profit