class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]

# intuition, tribonacci is just fibonacci but with 3 numbers and 3 base cases
# rather than using iteration, it's easier to use bottom up approach, since there are no new values during calculations
# since we have already set the base cases, and for each new iteration it is only using previously defined dictionary value