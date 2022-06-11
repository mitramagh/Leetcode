class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)-1):
            s=prices[i+1]-prices[i]
            if s>0:
                profit +=s
        return profit