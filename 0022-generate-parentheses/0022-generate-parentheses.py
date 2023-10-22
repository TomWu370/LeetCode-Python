class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        def traverse(n, pairs, open=0, close=0, temp=""):
            if close == n:
                pairs.append(temp)
                return

            if open < n:
                newTemp = temp + '('
                #print(f'open', temp)
                traverse(n, pairs, open+1, close, newTemp)

            if close < open:
                newTemp = temp + ')'
                #print(f'close', temp)
                traverse(n, pairs, open, close+1, newTemp)
            
        # default for open and close are 0
        traverse(n, pairs)

        return pairs

# learn binary expansion or dynamic programming
# just check if valid form when doing DP
# number of close can't exceed number of open
# while less than n, keep expanding it, and while close less than open, can append 1 close
# for each expansion, add 1 open, then if condition allow, add 1 close
# record number of open and close brackets
# Dynamic programming is all about the conditions
# need to separate the new temporary with previous temporary, so the 2 if statement can use the previous value
# rather than the changed value done in previous if statement