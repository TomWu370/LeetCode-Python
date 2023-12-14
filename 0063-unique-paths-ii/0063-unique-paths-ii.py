class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        switch = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                switch = True
            memo[(i, 0)] = 1 if not switch else 0
        switch = False
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                switch = True
            memo[(0, i)] = 1 if not switch else 0
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    memo[(i,j)] = 0
                else:
                    memo[(i, j)] = memo[(i-1, j)] + memo[(i, j-1)]

        return memo[(m-1, n-1)]

# same as unique paths 1, except we have to check whether the previous cell is an obstacle
# and for base case initialisation, we'll terminate once we reach an obstacle
# another solution could be to set the obstacle as having 0 paths to reach, then we can check for whether the previous cell
# has no path then set the cell to have 0, meaning 0 reachable paths
# make sure to set all the paths after the initialisation obstacle as 0 as well
# edge case involves starting cell is an obstacle, no valid paths


        