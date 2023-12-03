class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0

        for i in range(len(t)):
            if counter > len(s)-1:
                return True
            if t[i] == s[counter]:
                counter += 1
                continue
        if counter <= len(s)-1:
            return False
        return True
        

# have 2 pointers
# loop through subsequence manually with a counter
# then loop through sequence
# keep moving forward
# if counter reach beyond end of sub then return true
# if if current value of sequence is equal to sub then increment counter
# if counter is not beyond length of sub then return False
# default return True for single character s or t