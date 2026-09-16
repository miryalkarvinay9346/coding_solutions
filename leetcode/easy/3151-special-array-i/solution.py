class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        t=True
        for i in range(1,len(nums)):
            if nums[i]%2==nums[i-1]%2:
                t=False
                break
        return t
        