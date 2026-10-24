class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        c=0
        d=0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                c+=nums[i]
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                d+=nums[i]
        return (c-d)
                