class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = False
        head = 0
        tail = len(nums)
        while not found:
            print(nums[head:tail])
            middle = (head+tail) // 2
            print(middle)
            print(nums[middle])
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