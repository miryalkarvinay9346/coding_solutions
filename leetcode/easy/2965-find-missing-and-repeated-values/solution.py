class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        f=[0]*(n*n+1)
        a,b=0,0
        for i in grid:
            for j in i:
                f[j]+=1
        for i in range(1,n*n+1):
            if f[i]==2:
                a=i
            elif f[i]==0:
                b=i
        return [a,b]