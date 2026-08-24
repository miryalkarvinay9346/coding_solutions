class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            a=bin(i)
            if a.count('1')==k:
                c+=nums[i]
        return c