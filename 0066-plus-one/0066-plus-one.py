class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        max_idx = len(digits)-1
        for i in range(max_idx, -1, -1):
            if i == max_idx:
                sum = digits[i] + 1
            else:
                sum = digits[i] + carry

            if sum < 10:
                digits[i] = sum
                return digits
            else:
                carry = sum // 10
                digits[i] = sum % 10
                if i == 0:
                    return [carry] + digits

        return digits

# large integer
# increment by 1 then return the array
# essentially addition table
# no leading 0
# 1 method is to convert the array to integer then increment, but it may be a little bit slower
# therefore iterate through each digit, starting from last then increment, if result > 9 then carry over
# edge case, first iteration, rather than adding the carry add 1 instead
# edge case, if sum is less than 10 then loop complete, return
# edge case, if sum more than 10 then continue to carry over
# edge case, if the carry over process continues until the last digit, or i == 0, then return last carry digit combined with digits