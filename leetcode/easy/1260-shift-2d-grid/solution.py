class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m=len(grid)
        n=len(grid[0])
        for _ in range(k):
            last=grid[m-1][n-1]
            for i in range(m):
                for j in range(n):
                    grid[i][j], last = last, grid[i][j]
        return grid