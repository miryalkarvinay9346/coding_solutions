class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            k=abs(nums[i-1]-nums[i])
            if k>c:
                c=k
        if abs(nums[0]-nums[-1])>c:
            return abs(nums[0]-nums[-1])
        return c