class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         pro = prices[j] - prices[i]
        #         res = max(res, pro)
        # return res        
        l,r = 0,1
        mpr = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                pro = prices[r] - prices[l]
                mpr = max(pro,mpr)
            else:
                l=r
            r+=1
        return mpr
                
