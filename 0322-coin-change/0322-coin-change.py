class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[amount] == math.inf:
            return -1
        return dp[amount]

# this one requires exhaustive approach, with bottom up, requires updating established dp[i]
# when discover a better result
# this is where you need to use 2 for loops, 1st for updating the dp
# 2nd to update each index of dp to obtain the best possible value
# the 1st loop goes through the amount's range, updating the best coins for each of the possible numbers
# this means at 12, and [1,4,5], rather than greedy approach of 5,5,1,1, it will be 12 trying, 5,4,1
# 12-5 = 7, which requires 3 coins to complete, to total of 4
# 12-4 = 8, and 8 only requires 2 coins, therefore 3 in total, so 4,4,4 would win over 5,5,1,1 during iteration