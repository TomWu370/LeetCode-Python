class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # goes backwards
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= nums[i+1]:
                # keep going if next is more than current
                continue

            j = i+1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            
            # 1 line swap
            nums[i], nums[j-1] = nums[j-1], nums[i]
            # 1 line partial sort
            nums[i+1:] = reversed(nums[i+1:])
            return
                    
        nums.sort()

# intuition, start from last index, then compare to previous index, if larger then insert current index in front of previous index
# if not, continue going back the list
# until encounter a smaller value or no value found
# if found then insert like normal, however this would mean the value found is a few index behind the current index
# therefore take the difference between index then propagate through the list,swapping each pair, this will achieve inserting the 
# value inside the list
# if not then because of this special condition, all values should be in descending order now
# therefore return list sorted in ascending order as per requirements

# edge case 2,3,1
# even with the algorithm of swapping 2 with 3, to form 3,2,1 we're not done yet,
# in order to solve this problem, we just need to sort the items after 3, or the swapped value

# go through list, go to next index if the current is more than the next index down the list
# if the current index is more than the next left index, then set 2nd pointer to current +1
# move this 2nd pointer until we encounter a value that is less than or equal to current value
# then we swap these 2 values, then sort the rest of the list