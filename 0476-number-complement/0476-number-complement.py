class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        num = num.replace('1', '2')
        num = num.replace('0','1')
        num = num.replace('2','0')

        return int(num, 2)

# intuition, it's simply inverting the bits, we can convert the number to binary then remove the binary identifier string
# then replace the 1s with 0s and vice versa, then convert this string from binary to int