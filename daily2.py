# Timeout
from typing import List

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 1000000000


def dfs(x, y, grid, s, check):
    global answer
    if x == (len(grid) - 1) and y == (len(grid[0]) - 1):
        answer = min(answer, s)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and check[nx][ny] != -1:
            s += grid[nx][ny]
            check[nx][ny] = -1
            dfs(nx, ny, grid, s, check)
            check[nx][ny] = 0
            s -= grid[nx][ny]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        global answer
        check = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        check[0][0] = -1
        dfs(0, 0, grid, grid[0][0], check)
        tmp = answer
        answer = 1000000000
        return tmp


# g = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# g = [[1,2,3],[4,5,6]]
g = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]
print(Solution().minPathSum(g))
