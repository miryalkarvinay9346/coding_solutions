class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        c=0
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                if intervals[i][1]>=intervals[j][0] and intervals[j][1]>=intervals[i][0]:
                    c+=1
        return c