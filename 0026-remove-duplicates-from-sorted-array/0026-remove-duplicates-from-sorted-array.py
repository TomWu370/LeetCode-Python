class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

# Question expects inplace removal of list
# only need to return size of result list
# to perform inplace memory manipulation, we need to loop through the list and do it with indexes
# however the question only wants you to drag all the non duplicate items to the front in an ascending order
# the rest of the list after which will be ignored
# therefore we can keep a true index, j, go through the list
# then update the list when we encounter a value that's larger than the previous non duplicate value
# since the original list is also in ascending order, we won't encounter problem where future value are smaller
# then return j, as that is a counter for the final index, which is also the length of the final array