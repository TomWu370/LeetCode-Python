class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[:i-1])

        return max(dp)

# intuition, the base case is 1st value and 2nd value, the dp array should be the maximum money from that index
# sub problem is finding the maximum of all previous items excluding the one just before and adding the current money at ith index