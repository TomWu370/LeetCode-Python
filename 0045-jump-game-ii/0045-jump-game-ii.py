class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [math.inf] * len(nums)
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(nums[i]+1):
                if i+j < len(nums):
                    dp[i+j] = min(dp[i] + 1, dp[i+j])
        return dp[len(nums)-1]
            
# intuition, declare a empty list, opposite of what we're trying to achieve
# or the opposite or minimise, so infinite
# set base case as 0
# then iterate through the list, update all of the minimums
# for each step available, check if the step will cause index to go past target
# if not then update the current best steps, to be the minimum of previously possible defined minimum values
# all the way to the last item, which we return