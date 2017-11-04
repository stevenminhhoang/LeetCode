def to_binary(number):
    rem_stack = []
    ans = ""
    while number > 0:
        rem = number % 2
        rem_stack.append(rem)
        number = number // 2

    while rem_stack:
        ans = ans + str(rem_stack.pop())

    return ans

print(to_binary(8))
