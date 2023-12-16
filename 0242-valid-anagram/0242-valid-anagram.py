class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)
        return countS == countT

# intuition, to check whether something is anagram, you just need to see whether they have the exact same amount of characters
# this is where Counter comes into play, Counter provides the variety and quantity of characters in a string
# by comparing the 2 Counter dictionaries between the 2 string, we can know whether they have the same characters
        