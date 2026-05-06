#MY FIRST TRY
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        sell = prices[0]

        profit = 0

        for p in prices:

            if p < buy:
                buy = p
                sell = p
            
            elif p > sell:
                sell = p
                newprofit = sell - buy
                if newprofit > profit:
                    profit = newprofit

        return profit

#Common solution, slower
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        
