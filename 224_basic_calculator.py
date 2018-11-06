def calculator(s):
    res = 0
    sign = 1
    stack = []
    num = 0
    for char in s:
        if char == ' ':
            continue
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            res += sign * num
            num = 0
            sign = 1
        elif char == '-':
            res += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif char == ')':
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()

    if num != 0:
        res += sign * num

    return res

print(calculator("(1+(4+5+2)-3)+(6+8)"))
