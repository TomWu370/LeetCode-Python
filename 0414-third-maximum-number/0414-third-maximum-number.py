class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -math.inf
        second = -math.inf
        third = -math.inf

        for i in nums:
            if i == first or i == second or i == third:
                continue
            if i > first:
                third = second
                second = first
                first = i
            elif i > second:
                third = second
                second = i
            elif i > third:
                third = i
        return third if third > -math.inf else first
        