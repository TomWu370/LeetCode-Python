class Solution:
    def longestValidParentheses(self, s: str) -> int:

        pair = []
        stack = [0]*len(s)
        for i, val in enumerate(s):
            if not pair or val == '(':
                pair.append((i, val))
            elif val == ')':
                if pair[-1][1] == '(':
                    idx, _ = pair.pop()
                    stack[i], stack[idx] = 1,1
                else:
                    pair.append((i, ')'))
        ones, total = 0,0
        for i in stack:
            if i == 1:
                ones += 1
                total = max(total, ones)
            else:
                ones = 0
            
        return total

# intuition, push brackets to a stack, and have an array for confirmed pairs
# when a pair is found then change both indexes to 1, for confirmed pair
# loop through the pairs, tally up total pairs but start again when non pair detected, take the maximum of the previous and current
# pairs then start the total again
# 1 important detail to note is that, by storing both the value and original index, it's possible to update an array the same size
# as the original list, this is important for stack manipulations and operations