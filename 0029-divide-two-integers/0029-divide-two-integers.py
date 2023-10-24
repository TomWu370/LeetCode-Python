class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # handle obvious overflor
        if dividend > 2147483648-1:
            return 2147483647
        elif dividend < -2147483648:
            return -2147483648

        # handle ans calculation overflow
        if (dividend == -2147483648 and divisor == -1) or (dividend == 2147483648-1 and divisor == 1):
            return 2147483647

        ans = 0
        newDividend, newDivisor = abs(dividend), abs(divisor)
        
        while newDividend >= newDivisor:
            multiplier = newDivisor
            counter = 1

            while newDividend >= multiplier:
                newDividend -= multiplier
                multiplier += multiplier
                ans += counter
                counter += counter
        
        if (dividend < 0) ^ (divisor < 0):
            ans = -ans
        return ans 
        

# perform long division with subtraction
# to avoid dealing with both parameter being negative, get the absolute value of both at the start
# then only is negative then convert ans to negative
# in order to decrease the run time, increase the divisor each time, then for the last step do it step by step