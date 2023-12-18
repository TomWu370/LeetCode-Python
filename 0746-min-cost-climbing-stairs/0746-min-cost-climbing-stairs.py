class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [math.inf] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]) 
        return dp[-1]

# intuition, use dp and iterate through list updating minimum cost
# base case is 0 and 0 for 0 and 1 index
# sub problem identification, current index is dependent on the previous 2 indexes, since it's about minimum cost
# the current index is equal to the min of previous 2 indexes' cost, and plus their minimum cost
# so it would be getting the minimum of the previous indexes' cost and the total minimum cost to get to that index
# due to needing to reach the index beyond cost, or over the cost size, we need 1 extra index to iterate through, so len(cost)+1