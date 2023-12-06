class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(1, nums[i]+1):
                    # check if it's less than the target, if yes then that means you can still go forward
                    if i+j<n:
                        dp[i+j] = True
                    if i+j == n-1:
                        return True


        return dp[n-1]

        

# if jump is 0 then return False