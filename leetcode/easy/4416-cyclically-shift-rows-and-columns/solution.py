class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        a=[[0]*n for _ in range(n)]
        for i in range(n):
            k=rowShift[i]%n
            for j in range(n):
                a[i][j]=grid[i][(j+k)%n]
        b=[[0]*n for _ in range(n)]
        for j in range(n):
            k=colShift[j]%n
            for i in range(n):
                #k=colShift[j]
                b[i][j]=a[(i+k)%n][j]
        return b