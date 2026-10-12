

def maxProfit(prices: list[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if buy_price>p:
                buy_price=p
            
            max_profit = max(max_profit,p-buy_price)

        return max_profit

print(maxProfit([7,1,3,4,5,2]))