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

# intuition