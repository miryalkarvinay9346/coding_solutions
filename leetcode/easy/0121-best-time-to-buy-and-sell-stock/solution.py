class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=len(prices)-1
        m=0
        a=0
        while i<j:
            m=prices[j]-prices[i]
            a=max(m,a)
            if a>m:
                j-=1
            else:
                i+=1
        return a

