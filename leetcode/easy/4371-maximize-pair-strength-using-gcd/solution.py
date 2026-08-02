class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        m=0
        n=len(nums)
        for i in range(n):
            for j in range(n):
                k=(nums[i]*nums[j])//(gcd(nums[i],nums[j])**2)
                if k>m:
                    m=k
        return m
        