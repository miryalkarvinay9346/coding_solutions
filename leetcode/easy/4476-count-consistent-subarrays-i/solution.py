import math
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        c=0
        for i in range(len(nums)):
            #s=1
            for j in range(i+1,len(nums)+1):
                k=nums[i:j]
                s=k[0]
                for a in k:
                    s=s&a
                if s==min(k):
                    c+=1
        return c
                    