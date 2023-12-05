class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ranges = []
        start = ""
        for i in range(len(nums)):
            if not start:
                start = str(nums[i])

            if i == len(nums)-1 or nums[i+1] != nums[i]+1:
                if str(nums[i]) != start:
                    ranges.append(f'{start}->{nums[i]}')
                else:
                    ranges.append(start)
                start = None

        return ranges



# start = 0, or after first range, first item
# end = the index where next index is not current + 1 or if next is None/empty
# convert start to a string, this helps evaluating when start is 0
        