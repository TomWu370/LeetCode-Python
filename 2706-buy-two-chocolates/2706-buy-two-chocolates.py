class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        balance = money
        for i in range(2):
            if balance-prices[i] < 0:
                return money
            else:
                balance -= prices[i]
        return balance
        

# intuition, sort the prices
# then iterate through prices, if subtracting current item result in negative, then return money
# for loop for first 2 item, since questino only buys exactly 2 items
# so check for the smallest 2