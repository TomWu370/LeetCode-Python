class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sum = ""
        maxLength = max(len(num1), len(num2))
        carry = 0
        for i in range(maxLength):
            start1 = len(num1) - i -1
            start2 = len(num2) - i -1
            if (start1 < 0):
                tempSum = int(num2[start2]) + carry
            
            elif (start2 < 0):
                tempSum = int(num1[start1]) + carry
            
            else:
                tempSum =int(num1[start1]) + int(num2[start2]) + carry
            
            carry = tempSum // 10
            tempSum %= 10
            sum += str(tempSum)
        
        if (carry > 0):
            sum += str(carry)

        
        return sum[::-1]
        
# intuition is to iterate from the furtherest element, perform additions then move forward
# if can't go forward then ignore that number, or treat as 0