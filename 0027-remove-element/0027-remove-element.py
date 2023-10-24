class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)
        

# this question is similar to 26, where it wants inplace manipulations
# by using slicing, nums[:] then list comprehension this is considered inplace
# however if it's just nums then list comprehension it won't be
# by splicing the wanted values with list comprehension, it will not create a new list
# therefore we can easily manipulate the list with list comprehension