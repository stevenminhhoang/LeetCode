def cal_points(ops):
    stack = []
    for x in ops:
        if x == "+":
            stack.append(stack[-1] + stack[-2])
        elif x == "D":
            stack.append(stack[-1] * 2)
        elif x == "C":
            stack.pop()
        else:
            stack.append(int(x))

    return sum(stack)

print(cal_points(["5","2","C","D","+"]))
