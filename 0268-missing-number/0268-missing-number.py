class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        size = len(nums)
        actualTotal = (size * (size+1)) // 2
        return actualTotal - total
        