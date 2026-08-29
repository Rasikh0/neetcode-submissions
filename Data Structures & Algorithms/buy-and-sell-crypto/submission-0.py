class Solution: #two pointers, l = buy, r = sell
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0 #default case

        #keeps iterating till the end of prices array
        while r < len(prices): 
            if prices[l] < prices[r]: #checking if transaction is profitable
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: #when not a profitable transaction
                l = r #update the pointers
            r += 1
        return maxP
