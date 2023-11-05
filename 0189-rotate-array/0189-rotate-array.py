class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == 1 or k == 0:
            return
        print(nums[:k]) # up to k
        print(nums[:-k]) # up to -kth value
        print(nums[k:])
        print(nums[-k:])
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
            

# 99,-100,3,-1
# 99,-1,3,-100
# 99,-1,-100,3
# intuition, swap the subarray up to k with the subarray after k
# replace the subarray of value up to k, with value that are not affected by the shift, e.g. 1,2,3,4
# same with the other subarray
#1,2,3,4
#5,6,7
# [1, 2, 3]
# [1, 2, 3, 4]
# [4, 5, 6, 7]
# [5, 6, 7]
