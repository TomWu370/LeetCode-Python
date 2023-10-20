class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        sign = 1
        if num[0] == '-':
            sign = -1
            num = num[1:]
        num = int(num[::-1]) * sign
        if num > 2147483648-1 or num < -2147483648:
            return 0
        else:
            return num

# check if negative
# reverse as string
# check if in range
# if not return 0