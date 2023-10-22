class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        open = 0
        close = 0
        def traverse(n, pairs, open, close, temp):
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
            

        temp = ""
        traverse(n, pairs, open, close, temp)
        

        return pairs
        

# ()() = pairs
# (()) = house
# ()()() = n=2 + 1 pair
# ((())) = n=3 house
# (())() = n=3 - 1 house + pair
# ()(()) = n=3 - 1 house + pair reversed
# (()()) = n=3-1 pair + n=3-2 house

# learn binary expansion or dynamic programming
# just check if valid form when doing DP
# number of close can't exceed number of open
# while less than n, keep expanding it, and while close less than open, can append 1 close
# for each expansion, add 1 open, then if condition allow, add 1 close
# use count tuple to record number of open and close brackets
# Dynamic programming is all about the conditions