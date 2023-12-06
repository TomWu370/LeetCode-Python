class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = round(log(n, 3), 14)
        return x.is_integer()
  

# intuition, use logs, if result is int then found, and if less than or equal t0 then just return False
# log3(3^x) = x
# while this is a short solution, due to precision error, would require rounding, so not a complete solution