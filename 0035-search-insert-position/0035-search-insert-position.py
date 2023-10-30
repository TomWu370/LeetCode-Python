class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums)
        while True:
            middle = (head+tail) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                if middle+1 >= tail:
                    return middle+1
                head = middle + 1
            elif nums[middle] > target:
                if middle-1 < head:
                    return head
                tail = middle
        

# go in middle
# if not value then check if larger or smaller
# if smaller, discard larger values then recurse smaller half of list
# or just binary search

# intuition use binary sort as base, use 2 pointers to go through the list, this will preserve index values which is important
# for determining insert position
# pick the middle value
# if picked value is less than target then set head as middle +1, essentially discarding the lesser half
# vice versa for more than target
# but if adjusting head or tail will reach an edge, e.g. adjusting head will reach tail then return middle index + 1
# if adjusting tail will touch the head, then return the head, or current head positino will be replaced by this smaller value
# 1 important thing to note is that, the comparison for tail touching head is less than without equal, this eliminates -1 index