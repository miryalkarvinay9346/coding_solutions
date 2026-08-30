class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        s=0
        m=(10**9)+7
        for i in range(len(nums)):
            w=nums[i]%10
            d=math.floor(nums[i]/10)
            l=str(d)
            x=int(l[:w])
            y=int(l[w:])
            s=(s+pow(x,y,m))%m
            #return x,y
        return s