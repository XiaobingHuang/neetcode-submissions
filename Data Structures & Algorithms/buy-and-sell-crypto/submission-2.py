class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r]>prices[l]:
                MAX = max(MAX, prices[r]-prices[l])
            else:
                l = r
        return MAX



            


        