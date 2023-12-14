class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        for i in range(m):
            memo[(i, 0)] = 1
        for i in range(n):
            memo[(0, i)] = 1

        for i in range(1, m):
            for j in range(1, n):
                memo[(i, j)] = memo[(i, j-1)] + memo[(i-1, j)]
        return memo[(m-1, n-1)]

# intuition
# with DP, if it's finding optimal solution then you only need for loops
# if finding total number then you need memoisation
# * can't guarantee for all problems but this is a general way to go at DP
# the robot can only go right or down
# after setting the base case to equal to the starting position and equal 1
# the rest of the chart fill up by itself, we just need to traverse the chart
# for every downward movement, move all the way to right, and update the current cell with the total number of path from previous
# up or left cells, after setting up the base cases, we will always have 2 possible paths to a cell