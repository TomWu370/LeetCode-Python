class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        maximum = 0
        for price in prices[1:]:
            if start < price:
                maximum = max(maximum, price-start)
            else:
                start = price
        return maximum

# 2 pointer
# sliding window
# recursion
# for recursion
# similar to 2 pointer
# check if i is more than j or j more than length if so then end recursion
# set i to 0 and j to i+1
# if i is less than j value, then calculate maximum, then move j along the list
# otherwise, restart the list but move i to the next value
# due to the nature of the list, the list has to progress from left to right, can't have j go from last index and move left
# otherwise some pair would be missed

# have to use 2 pointer version, due to python's maximum recursion limit
# go through list with 2 pointer, move 2nd pointer continuously right
# if current i is too large then move i along