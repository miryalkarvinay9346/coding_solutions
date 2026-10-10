class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        b=float('-inf')
        a=[-1,-1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and nums[i]>nums[j] and i!=j:
                    c=nums[i]*nums[j]
                    if c>b:
                        b=c
                        a=[i,j]
        return a
                    
                    