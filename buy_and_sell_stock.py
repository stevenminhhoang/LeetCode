def buy_and_sell_stock(arr):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(arr)):
        min_price = min(min_price, arr[i])
        max_profit = max(max_profit, arr[i] - min_price)

    return max_profit

print(buy_and_sell_stock([7,1,5,3,6,4]))
