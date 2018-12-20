def operation(operator, x, y):
    if operator == "+":
        return x + y

    elif operator == "-":
        minus = -1
        add = 1
        if y == 0:
            return x
        elif y > 0:
            while y > 0:
                x += minus
                y = y + minus
        else:
            while y < 0:
                x += add
                y = y + add

        return x

    elif operator == "*":
        temp = x
        count = 1
        while count < y:
            x += temp
            count += 1

        return x

    elif operator == "/":
        ans = 0
        while x >= y:
            temp = y
            val = 1
            while x >= temp + temp:
                temp += temp
                val += val

            ans += val
            x -= temp

        return ans

print(operation("-", 5, 2))
print(operation("*", 5, 5))
print(operation("/", 20, 5))
