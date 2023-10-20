class Solution:
    def myAtoi(self, s: str) -> int:
        OPERATION = None
        operation_map = {'+':1, '-':-1}
        operation_check = False
        number = None
        s = s.lstrip()
        for char in s:
            if not operation_check:

                if char in operation_map:
                    OPERATION = operation_map[char]
                else:
                    if char.isnumeric() and char != "0":
                        number = char
                    elif not char.isnumeric():
                        return 0
                    OPERATION = 1
                operation_check = True
            else:
                if char.isnumeric():
                
                    if char == "0" and not number:
                        pass
                    elif not number:
                        number = char
                    elif number:
                        number += char

                elif not char.isnumeric() or char.isspace():
                    if number and int(number)>0:
                        break
                    else:
                        return 0
        if not number:
            return 0
        
        number = int(number) * OPERATION
        if number < -2147483648:
            number = -2147483648
        elif number > 2147483647:
            number = 2147483647
                
        return number
        

# loop through each char
#1- if whitespace then ignore
#2- have operation as -1 or 1, then multiply in end
# if OPERATION is none then when read - or + update, otherwise ignore
#3- read digit until not digit then break
#4- if number digit string is None and 0 is read then ignore
# by doing char == "0"
#5- convert integer then check within range, if less or more than limit then clamp
#6- return integer