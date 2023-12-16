class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        for i in range(1, n+1):
            if i == 1:
                memo[i] = 1
            elif i == 2:
                memo[i] = 2
            else:
                memo[i] = memo[i-1] + memo[i-2] 
        return memo[n]
        

# intuition, since it talks about total number of ways, we should use memoisation
# sub problem is the current n number of ways is the combination of n-1 ways and n-2 ways
# the base case is i = 1 and i = 2, which is 1 and 2 respectively