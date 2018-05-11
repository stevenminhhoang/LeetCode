def max_profit(prices):
    max_p = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            max_p += prices[i+1] - prices[i]

    return max_p


price = [7, 1, 5, 3, 6, 4]
print(max_profit(price))
