class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        dp.append([1])
        for i in range(1,numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(dp[i-1][j-1] + dp[i-1][j])
            else:
                temp.append(1)
            dp.append(temp)
        return dp

# intution use list and iterate through nmber of rows
# base case is 1, and then for each other row set the first and final item to be 1 and assign other necessary values
# then for each sub problem, the current value is equal to previous row's j-1 item + jth item
# to populate the rows, start from 1, then have a for else closure to append the 1