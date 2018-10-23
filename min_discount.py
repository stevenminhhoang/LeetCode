# O(n)
def min_discount(prices):
    ans = 0
    stack = []
    for i in reversed(range(len(prices))):
        while stack and stack[-1] > prices[i]:
            stack.pop()
        if stack:
            ans += prices[i] - stack[-1]
        else:
            ans += prices[i]
            print("Index not on discount:", i)

        stack.append(prices[i])

    return ans

print(min_discount([5, 4, 5, 1, 3, 3, 8, 2]))
