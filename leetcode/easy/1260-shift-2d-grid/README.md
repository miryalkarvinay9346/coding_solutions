# Shift 2D Grid

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a 2D `grid` of size `m x n` and an integer `k`. You need to shift the `grid` `k` times.

In one shift operation:

- Element at grid[i][j] moves to grid[i][j + 1].
- Element at grid[i][n - 1] moves to grid[i + 1][0].
- Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the  *2D grid*  after applying shift operation `k` times.

 

 **Example 1:** 

```
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

```

 **Example 2:** 

```
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

```

 **Example 3:** 

```
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m <= 50
- 1 <= n <= 50
- -1000 <= grid[i][j] <= 1000
- 0 <= k <= 100

## Solution

**Language:** Python  
**Runtime:** 104 ms (beats 12.99%)  
**Memory:** 19.3 MB (beats 94.59%)  
**Submitted:** 2026-11-26T13:17:33.638Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/shift-2d-grid/)