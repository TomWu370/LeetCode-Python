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
        result = []
        i=0
        letters = numToLet[digits[i]]

        def traverse(let, i):
            letters = numToLet[digits[i]]
            for l in letters:

                if i < len(digits)-1:
                    # recursively go down the digit depth, with previous letter + current letter
                    traverse(let+l, i+1)
                # only start appending to final list when end is reached
                else:
                    result.append(let+l)
            return result

        # start with first digit
        for let in letters:
            # 2 or more digits
            if i < len(digits)-1:
                traverse(let, i+1)

            # 1st iteration takes care of single digit
            else:
                result.append(let)
                 
        return result

# digit are only in range of 2-9 therefore we only care about the alphabet
# the length of digits determines the length of the output items in the output list
# Need to have dynamic mehod that expands as we have more digits
# for the first letter, get lists of available item, then for each item, recursively call a method that will do the same but for next item
# 2,3,
# abc, def, ghi
# a, ad, adg, adh, adi, ae, aeg,....
# start with first letter, then pass current letter to next recursive method call, then if there are more depth
# pass the previous letter + current letter as the new letter
# repeat until end of depth is reached, then append the current letter with each new letter