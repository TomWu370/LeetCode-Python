class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ranges = []
        start = ""
        for i in range(len(nums)):
            if not start:
                start = str(nums[i])

            if i < len(nums)-1 and nums[i+1] != nums[i]+1:
                rang = f'{start}'
                if str(nums[i]) != start:
                    rang += f'->{nums[i]}'
                ranges.append(rang)
                start = None
            elif i == len(nums)-1:
                rang = f'{start}'
                if str(nums[i]) != start:
                    rang += f'->{nums[i]}'
                ranges.append(rang)
                start = None
        return ranges



# start = 0, or after first range, first item
# end = the index where next index is not current + 1 or if next is None/empty
        