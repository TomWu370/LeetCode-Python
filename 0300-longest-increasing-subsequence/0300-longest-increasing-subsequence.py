class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)

# intuition, have a dp list that records the total number of preceding decreasing values for that index
# start from 1 to length of nums, updating each index, with how many decreasing value precede the current index
# base case is index of 0 is 1
# sub problem, for current index, loop through values before the current index, check if less than current value
# if so then update the index with the value of the index with a smaller value plus 1, but pick the maximum result from
# all the preceeding values