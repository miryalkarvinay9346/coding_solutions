class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        c=0
        for i in range(len(nums)):
            k=nums[i]
            if -k in nums:
                return k
        return -1