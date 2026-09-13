class Solution:
    def count_non_minimum(self, nums):
        # write your code here
        m=min(nums)
        cm=nums.count(m)
        return len(nums)-cm