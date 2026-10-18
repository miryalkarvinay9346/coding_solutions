class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            if nums[i]^nums[i+1]<=0:
                c+=1
        return c
                
            
            
            