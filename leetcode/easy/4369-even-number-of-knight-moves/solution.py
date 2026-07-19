class Solution(object):
    def canReach(self, start, target):
        """
        :type start: List[int]
        :type target: List[int]
        :rtype: bool
        """
        #logic is if start and end have same color , answer is true else false
        #to check color (x+y)%2 , if even - same colour , else other color
        if (start[0]+start[1])%2==(target[0]+target[1])%2:
            return True
        else:
            return False
            