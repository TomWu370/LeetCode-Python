class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        for j in range(1,len(prices)):
            if j <= len(prices)-2 and prices[j+1] < prices[j] and prices[i] < prices[j]:
                profit += (prices[j] - prices[i])
                i = j+1

            else:
                if prices[i] < prices[j]:
                    profit += (prices[j] - prices[i])
                i = j
        return profit

# if continuous list then keep going until end
# if bumpy then take multple stock, check if next price is less than current, if so then sell current stock then buy next stock
# if j is less than i then move i along and make j to i + 1, and restart iteration

# intuition, loop through prices like in 121, except for the if loop, check the next 2 values, so make sure the current
# j is within range
# if the next j value is more than the current j, then tally up the current stock price, then move i to the next j/buy next j stock
# if the 3rd condition is to make sure descending list aren't taken into account
# in the else statement, check whether the i is less than j value, this takes care of ascending list, as there are no stopping
# value for ascending list, asc and desc list are edge cases for this question
# if i is less than j in ascending list then tally up the whole list until it's not ascending
# finally move the i value along 1, to restart the list