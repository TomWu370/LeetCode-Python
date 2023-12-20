class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        power = math.log2(n)
        return floor(power) == ceil(power)

# intuition,use log2, if log2 result is int then return True
# 2^x = result
# log2(2^x) = x