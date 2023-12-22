class Solution:
    def maxScore(self, s: str) -> int:

        scores = []
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            print(left)
            print(right)
            scores.append(left.count('0')+right.count('1'))
        print(scores)
        return max(scores)

# intuition, iterate through splitting string, start from 1
# keep record of number of 0 on left and number of 1 on right, sum of those 2 number is the total for this split
# keep record of all the splits, then return the max of the list
# edge case, when length is less than 3, return the max of 1 counts or 0 counts