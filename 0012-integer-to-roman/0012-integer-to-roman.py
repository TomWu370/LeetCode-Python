class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = {'1':'I',
                      '5':'V',
                      '10':'X',
                      '50':'L',
                      '100':'C',
                      '500':'D',
                      '1000':'M',}
        answer = ""
        num = str(num)
        for i in range(len(num)-1, -1, -1):
            j = len(num)-1 - i

            if int(num[j]) < 4:
                answer += conversion[str(10**i)] * int(num[j])
            elif int(num[j]) == 4:
                answer += conversion[str(10**i)] 
                answer += conversion[str((10**i)*5)]
            elif int(num[j]) < 9:
                answer += conversion[str((10**i)*5)]
                answer += conversion[str(10**i)] * (int(num[j])-5)
            elif int(num[j]) == 9:
                answer += conversion[str(10**i)] 
                answer += conversion[str((10**i)*10)]
        return answer

# dictionary for conversion
# when encounter 4 or 9, when 4 add current digit 1 then add current digit 5, 
# when 9, add current digit 1 then add current digit 1 *10
# when < 9 and > 4, add current digit 5 then add current single digit number - 5 of current digit 1
# keep a counter of the current nth, for example 2nd digit means it's 10*digit which is i
# i represent the current digit
# j represent the current value, i and j are opposite, as i go up, j goes down
# scanning through each digit with j in descending order
# i keeps a count of how large the current digit is