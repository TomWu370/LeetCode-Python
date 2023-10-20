class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s):
            return s == s[::-1]
            
        for window in range(len(s), -1, -1):
            for start in range(0, len(s)-window+1):
                end = start + window
                if palindrome(s[start:end]):
                    return s[start:end]