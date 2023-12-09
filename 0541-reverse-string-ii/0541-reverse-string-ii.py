class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""

        for i in range(0, len(s), 2*k):
            ans += s[i:i+k][::-1]
            ans += s[i+k:i+2*k]
            
        return ans
# if less than k character then return reversed
# if less than 2k but more than k, then reverse first k characters
# for every 2k character slices, reverse the first k characters then move on to next 2k slices

# intuition here is that you can get a slice of a string, then you can reverse that slice in the same line, you add that 
# to a final answer string
# then you add the remaining unaltered characters with the current step to the answer string
# as it turns out, this works because you're traversing every 2k of a window within the given string
# then you take k of that slice, then the rest of that slice
# when slicing it doesn't matter if the size is over the length, it simply ignores and returns the max length
# therefore there is no need to use if loops to check for ranges or conditions