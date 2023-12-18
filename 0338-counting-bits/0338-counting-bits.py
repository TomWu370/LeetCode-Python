class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0 for _ in range(n+1)]
        dp[1] = 1

        for i in range(2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + 1
        return dp

        

# intuition, for odd numbers, it's dependent on num//2, then + 1, since the extra dimension of 10s comes from the number being
# powers of 2s
# intuition 2, for a number 5, get the binary of that number, then calculate the total 1s downward
# for even number it can be thought of number//2
# base case is [1]