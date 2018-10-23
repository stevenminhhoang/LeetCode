def calculator(s):
    s = s.strip()
    num, stack, sign = 0, [], '+'
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if s[i] in ('+', '-', '*', '/') or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            else:
                # Truncate towards zero
                stack.append(int(stack.pop() / num))
                # temp = stack.pop()
                # if temp // num < 0 and temp % num != 0:
                #     stack.append(temp // num + 1)
                # else:
                #     stack.append(temp // num)


            num = 0
            sign = s[i]

    return sum(stack)

print(calculator("3-2*2*2/4"))
