class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0,1]
        for i in range(2, n+1):
            if i % 2 == 0:
                dp.append(dp[i//2])
            else:
                dp.append(dp[i//2] + dp[i//2+1])
        return max(dp)
        
# a simple bottom up dynamic programming problem, which is simply a loop iteration with reference to previous values
# however the difficulty comes at recognising the requirement in the question