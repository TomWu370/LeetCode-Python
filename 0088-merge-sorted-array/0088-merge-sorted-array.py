class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, end = m-1, n-1, m+n-1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[j]
                j -=1
            end -= 1

# go through both list, only go to next item if the other list's current item is more than the current list
# use 3 pointer method, but have the 3rd pointer stationary and go through m items
# continue until all items in 2nd list is added to 1st list
# start from back where all the zeroes are at, this will provide a safe environment to manipulate list1
# if current i value is more than j value then use the i value as the current value for the end index
# otherwise choose the j value to be the end index value