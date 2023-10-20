class Solution:
    def romanToInt(self, s: str) -> int:
        order = {'M':1000,
                'D':500,
                'C':100,
                'L':50,
                'X':10,
                'V':5,
                'I':1}
        sum = 0
        for i in range(len(s)):
            current = s[i]
            if i+1 < len(s):
                next = s[i+1]
                next_num = order[next]
            else:
                next_num = 0
            number = order[current]

            if next_num > number:
                sum -= number
            else:
                sum += number
        
        return sum


# loop through all letters
# if index for letter is after previous letter like V being bigger than I but it comes after
# then switch position then subtract
# rather than the current approach of ignoring the next digit if subtraction is detected
# just detect next digit and apply subtraction to current digit
# sum = 0
# previous = math.inf
# for i in range(len(s)):
#     current = s[i]
#     if i+1 < len(s):
#         next = s[i+1]
#         next_num = order[next]
#     else:
#         next_num = 0
#     number = order[current]


#     if next_num > number:
#         sum += next_num - number
#         previous = number
#     elif previous < number:
#         pass
#     else:
#         sum += number