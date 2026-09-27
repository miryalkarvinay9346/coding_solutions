class Solution:
    def intersect(self, nums1, nums2):
        # write your code here 
        a=list(set(nums1) & set(nums2))
        a.sort
        return a
        