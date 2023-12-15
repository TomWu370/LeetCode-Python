class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = ()
        ans = 0
        squares = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] >= 0:
                    squares += 1

        def recurse(pos, grid, squares):
            nonlocal ans

            if grid[pos[0]][pos[1]] == 2:
                if squares == 1:
                    ans += 1
                return
            
            prev = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = 1
            squares -= 1


            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    ni, nj = pos[0] + i, pos[1] + j
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] in {-1, 1}:
                        continue
                    recurse((ni, nj), grid, squares)
            # after recursion finish, reset the first starting position to original value, this will be done for all squares in path
            grid[pos[0]][pos[1]] = prev

        recurse(start, grid, squares)
        return ans

# intuition, similar to unique paths 2, we have an obstacle square, treatment should be the same as before
# the problem really starts to differentiate when the objective was to walk over every non obstacle square exactly once
# this is no longer a DP problem
# to start we should find the starting position first
# then count the total number of squares to actually traverse
# have 2 more variables, the answer for total number of paths, and the currently explored squares
# recursively traverse all possible paths then simply count the numbers of total paths
# if encounter obstacle or goal then return
# the most crucial part is to assign the visited square as visited by setting it as a ignoring value, or simply same as start