class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = None
        current = ""
        for i in range(len(s)):
            current = s[i]

            for j in range(i+1, len(s)):
                if s[j] not in current:
                    current += s[j]
                    if not longest or len(current) > len(longest):
                        longest = current

                else:
                    break

        if not longest or len(current) > len(longest):
            longest = current


  
        return len(longest)

# keep track of longest substring
# compare string, return first occurence of non repeating
