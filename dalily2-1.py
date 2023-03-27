from typing import List

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]

        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[len(grid) - 1][len(grid[0]) - 1]


# g = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# g = [[1,2,3],[4,5,6]]
g = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]
print(Solution().minPathSum(g))