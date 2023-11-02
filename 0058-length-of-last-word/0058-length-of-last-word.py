class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(filter(None, s.split(' ')))
        return len(words[-1])


# essentially delimit by space then return last item in list
# and finally, remove empty strings for edge cases where there are space at the end
# use filter to replace easily, wrap result with list to get the final list