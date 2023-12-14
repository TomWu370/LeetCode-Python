class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [ [math.inf]*n for i in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    # set starting point
                    dp[0][0] = grid[0][0]
                # since you can only move down or right, therefore the best path for straight down is itself + previous cell
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    # update current cell with the minimum of the result of previously going down or right
                    dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
        # return result for final cell
        return dp[m-1][n-1]
        