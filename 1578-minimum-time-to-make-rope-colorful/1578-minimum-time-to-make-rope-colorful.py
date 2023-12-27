class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                if neededTime[i] > neededTime[i-1]:
                    total += neededTime[i-1]
                    neededTime[i-1] = neededTime[i]
                else:
                    total += neededTime[i]
                    neededTime[i] = neededTime[i-1]

        return total

# intuition, have a stack, record current colour, if current is same as previous then push to stack,if stack not empty
# then consume the stack, however only pop out the minimum time, until stack if 1

## new intuition, rather than comparing the next value with the current, and having a stack, it's easier
# to just perform the min operation with the times when you encounter atleast 1 of the same colour
# however with multiple of the same colour, the popped or consumed balloon should disappear from list
# to emulate this behaviour, simply replace the value at that position with the larger value
# stack of [0,1] -> [b,b] -> [1,2]