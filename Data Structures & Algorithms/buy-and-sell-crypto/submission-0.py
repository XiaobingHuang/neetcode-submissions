class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        MAX = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] > 0:
                MAX = max(MAX, prices[r] - prices[l])
            else:
                l = r
        return MAX



            


        