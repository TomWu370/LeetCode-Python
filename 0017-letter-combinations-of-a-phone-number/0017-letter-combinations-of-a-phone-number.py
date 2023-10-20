class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        numToLet = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']}

        def traverse(let, i, digits, numToLet, result):
            letters = numToLet[digits[i]]
            for l in letters:

                if i < len(digits)-1:
                    traverse(let+l, i+1, digits, numToLet, result)
                elif i == len(digits)-1:
                    result.append(let+l)
            return result

        result = []
        i=0
        letters = numToLet[digits[i]]
        # still digits down the chain
        for let in letters:
            # 2 or more digits
            if i < len(digits)-1:
                traverse(let, i+1, digits, numToLet, result)

            # 1st iteration takes care of single digit
            else:
                result.append(let)
                 
        return result


# digit are only in range of 2-9 therefore we only care about the alphabet
# the length of digits determines the length of the output items in the output list
# Need to have dynamic mehod that expands as we have more digits
# for the first letter, get lists of available item, then for each item, recursively call a method that will do the same but for next item
# use while loop to increment i until it reaches end of list
# 2,3,4
# abc, def, ghi
# for 2, with a, 3 exist
# a, ad, adg, adh, adi, ae, aeg,....
# pick first element then move onto next element
# pick first letter, then move to next digit if not end, then fill first letter with 2nd letters, return list when end
# otherwise continue process