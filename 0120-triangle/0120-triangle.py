class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[math.inf]*len(row) for row in triangle]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):

            for j in range(len(triangle[i])):
                if 0 <= j-1 and j < len(triangle[i-1]):
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                elif 0 <= j-1:

                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]

        return min(dp[-1])

# intuition, use dp list, traverse through each value row by row
# base case, top of triangle, sum = 2
# sub problem, each index will take minimum of previous adjacent values, for examle at row 3, val 5
# take min of adding row 2, val 3,4
# initialise dp 2d list with variable sized rows
# add check for whether the previous adjacent values exists
# then return the minimum of the last row