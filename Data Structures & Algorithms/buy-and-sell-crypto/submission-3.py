class Solution: #two pointers, l = buy, r = sell
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices): 
            # protfitable 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: # not profitable
                l = r
            r += 1
        
        return maxP


