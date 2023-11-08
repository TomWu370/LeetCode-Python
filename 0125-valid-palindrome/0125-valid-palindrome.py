class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        return s == list(reversed(s))

# convert to lower case
# pick out alphanumeric characters then form a list
# return true of reversed s vs normal s
# list(reversed(s)) is more efficient than s[::-1]