class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        memo = {}
        
        for i in range(1, n+1):
            if i <=2:
                result = 1
            else:
                result = memo[i-1] + memo[i-2]
            memo[i] = result
        return memo[n]
    
# memoisation with DP