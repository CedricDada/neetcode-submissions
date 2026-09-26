class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        def dfs(i, j):
            area = 0
            if ((i,j) not in visited):
                area += 1
                visited.add((i,j))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    area += dfs(i, j-1)
                if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                    area += dfs(i, j+1)
                if i-1 >= 0 and grid[i-1][j] == 1:
                    area += dfs(i-1, j)
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    area += dfs(i+1, j)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res

