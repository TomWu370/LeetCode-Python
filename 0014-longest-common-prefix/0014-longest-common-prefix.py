class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        minStr = min(strs)
        strs.remove(minStr)
        for j in range(len(minStr), -1, -1):
            prefix = minStr[0:j]
            for s in strs:
                if prefix != s[0:j]:
                    found = False
                    break
                found = True
            
            # no error therefore loop done, therefore found
            if found:
                return prefix
        return "" 

# i = 0, since it's prefix i stays at 0
# declare a for loop going backwards from length of the smallest item, this is because smaller item can't contain more letter than the longer one
# for each substring, check if prefix exist in all other items, if true then return prefix, if none found return empty string or move to next substring
# the intuition here is to realise that for all of condition to be true, you just need to find 1 counter example, and doing all or counter example
# will both go through the whole list, but one is easier to implement
# to improve run time use break to skip loop if check is complete