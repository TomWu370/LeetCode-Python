class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        latest = None
        valid = {'(':')',')':'(','{':'}','}':'{','[':']',']':'['}
        for i in s:
            if i in {'(','{','['}:
                parentheses.append(i)
                latest = i

            # when opposite
            elif latest and i == valid[latest]:
                parentheses.pop()
                latest = None if not parentheses else parentheses[-1]
            else:
                return False
        if parentheses:
            return False
        else:
            return True

        

# loop through string append parenthese character to a list in order
# record latest parenthesis character, if the next one is the same type then can pop the current one from list
# then update latest as current last in the list
# or update latest when encounter new type of open bracket
# if encounter any wrong condition then can return False, otherwise continue
# final edge case where there is only 1 parentheses, check if final parentheses is empty or not
# if empty then it means all the pairs have been matched and eliminated, otherwise return False