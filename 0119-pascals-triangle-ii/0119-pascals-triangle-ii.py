class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] for _ in range(rowIndex+1)]

        for i in range(1, rowIndex+1):
            for j in range(1, i):
                dp[i].append(dp[i-1][j-1] + dp[i-1][j])
            else:
                dp[i].append(1)

        return dp[rowIndex]
        

# intution, use the code for pascal's triangle 1, however this is a only return the index of the dp 2d array
# but rowIndex is still the same as n rows to be generated, so essentially the same code here
# since the first row is always 1, initialise a dp 2d list to have 1 as the starting value
# due to range not being inclusive because of 0 indexed, rowIndex of 3 actually means 4 lists, therefore we need to
# calculate rowIndex+1 amount of rows