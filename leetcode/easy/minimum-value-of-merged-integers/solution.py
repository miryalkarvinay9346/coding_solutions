class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        c=[]
        for i in range(0,len(nums)-1,2):
            c.append(int(str(nums[i])+str(nums[i+1])))
        return min(c)