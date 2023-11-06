class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profits = [0]
        tempProfit = 0
        for j in range(1,len(prices)):
            print(f'i: ',i,' :',prices[i])
            print(f'j: ',j,' :',prices[j])
            if j <= len(prices)-2 and prices[j+1] < prices[j] and prices[i] < prices[j]:
                profits.append(prices[j] - prices[i])
                print(profits)
                i = j+1
                
            # if prices[i] < prices[j]:
            #     profit = max(profit, prices[j] - prices[i])
            else:
                if prices[i] < prices[j]:
                    tempProfit = max(tempProfit, prices[j] - prices[i])
                    profits.append(tempProfit)
                    print(profits)
                    tempProfit = 0
                i = j
        return sum(profits)

# i:  0  : 7
# j:  1  : 1

# i:  1  : 1
# j:  2  : 5

# i:  3  : 3
# j:  3  : 3

# i:  3  : 3
# j:  4  : 6

# i:  4  : 6
# j:  5  : 4


# if continuous list then keep going until end
# if bumpy then take multple stock, check if next price is less than current, if so then sell current stock then buy next stock
# if j is less than i then move i along and make j to i + 1, and restart iteration