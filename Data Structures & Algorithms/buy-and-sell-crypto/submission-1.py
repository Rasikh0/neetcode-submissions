class Solution: #two pointers, l = buy, r = sell
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]: # if profitable transaction
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: # if not profitable transaction prices[l] > prices[r]
                l = r
            r += 1
        return maxP

