class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        i = 0
        j = len(height)-1
        while i<j:
            answer = max(answer, min(height[i], height[j])*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return answer



# find 2 line that gives the largest area
# return max area
# difference in i = length
# height = min (x, y)
# dual pointer technique, move 2 point towards the middle, but only 1 at a time according to certain condition