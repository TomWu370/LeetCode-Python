class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

        
# sort list, then pick out middle element, since it always appears more than half the list, it will always appear in middle