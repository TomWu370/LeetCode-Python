class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for key in counts:
            if counts[key] >= 2:
                return True
        return False
        

# intuition use Counter, then iterate through values return true if more than 2
# otherwise return false