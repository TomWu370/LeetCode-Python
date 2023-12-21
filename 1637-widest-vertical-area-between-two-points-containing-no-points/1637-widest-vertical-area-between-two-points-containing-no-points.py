class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arry = []
        for i in range(len(points)):
            arry.append(points[i][0])
        arry.sort()
        max_diff = 0
        for i in range(1, len(arry)):
            if arry[i] - arry[i-1] > max_diff:
                max_diff = arry[i] - arry[i-1]
        return max_diff


# intuition, for each pillar, find the largest width