class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        for i in range(len(haystack)-window+1):
            if haystack[i:i+window] == needle:
                return i
        return -1 
            
        

# intuition
# iterate through haystack, since needle is always smaller than haystack, we can assume false if needle larger than haystack
# however when needle is larger than haystack, the for loop will not work anyway so can ignore this check
# for each index of haystack, extend a window of size needle, check if it's valid, if so then return i
# set i to be 0 up to len haystack - len needle, and +1 since it's 0 index, we will be able to reach the last element with +1
# if nothing is found then by default return -1