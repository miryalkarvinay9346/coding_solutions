class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            k=str(i)
            if len(k)%2==0:
                c+=1
        return c        
        