class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = ""
        currChar = chars[0]
        count = 0
        for char in chars:
            if char == currChar:
                count += 1
            else:
                ans += currChar 
                if count > 1:
                    ans += str(count)
                currChar = char
                count = 1
        else:
            ans += currChar
            if count > 1:
                ans += str(count)

        for i in range(len(ans)):
            chars[i] = ans[i]
        chars[:] = chars[:len(ans)]
        return len(chars)

# intuition you don't need to create the array, only need to pop all the values into a single string, then compute length
# this can be done via a Counter, then go through the Counter object, add the key value pair to a string, but ignore value if 1 *
# that would only work for non in place question
# in this case for inplace, it's possible to iterate through the string, then replace each index of the array
# as for the rest of the indexes, simply perform a inpalce slice afterwards or before
# edge case, non consecutive repeat characters, rather than using Counter, which only allows the same character once
# go through the list, and count yourself, with reference to a variable called current_char
# rather than using a list, simply modify the result by checking for if count is more than 1