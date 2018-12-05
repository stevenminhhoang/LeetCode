def removeKdigits(num, k):
    if k == len(num):
        return "0"

    stack = []
    i = 0
    while i < len(num):
        while k > 0 and stack and stack[-1] > num[i]:
            stack.pop()
            k -= 1

        stack.append(num[i])
        i += 1

    while k > 0:
        stack.pop()
        k -= 1

    j = 0
    while j < len(stack) - 1 and stack[j] == "0":
        j += 1

    return "".join(stack[j:])

print(removeKdigits("1432219", 4))
