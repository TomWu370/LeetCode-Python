class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

# for loop loop through all possibility
# for loop for each item, find target - item, if that result exist in list return idx and item idx # Correct answer
# use hashmap:
# 1) to get index information for whether values exist or not
# 2) efficiency
        