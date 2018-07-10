def change(coins, amount):
    memo = {}
    return change_helper(coins, amount, 0, memo)

def change_helper(coins, amount, index, memo):
    if amount == 0:
        return 1

    if index >= len(coins):
        return 0

    key = (amount, index)
    if key in memo:
        return memo[key]

    amount_with_coin = 0
    count = 0
    while amount_with_coin <= amount:
        remaining = amount - amount_with_coin
        count += change_helper(coins, remaining, index + 1, memo)
        amount_with_coin += coins[index]

    memo[key] = count

    return count


print(change([1, 2, 5], 5))
