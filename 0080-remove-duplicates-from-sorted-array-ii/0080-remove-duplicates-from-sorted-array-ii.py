class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = Counter(nums)
        counter = 0
        for i in range(len(nums)-1):
            if counts[nums[i]] > 2:
                counts[nums[i]] -= 1
                nums[i] = 999999999
                counter += 1
        nums.sort(reverse=False)
        return len(nums) - counter
        

# use dictionary to record occurence
# each time extra is discovered substring the list