# O(n)
def calculate(s):
    def operation(sign, second, first):
        if sign == "+":
            return first + second
        elif sign == "-":
            return first - second
        elif sign == "*":
            return first * second
        elif sign == "/":
            return first // second

    def precedence(op):
        if op == "+" or op == "-":
            return 1
        elif op == "*" or op == "/":
            return 2

        return 0

    nums, ops = [], []
    i = 0
    while i < len(s):
        char = s[i]
        if char == " ":
            i += 1
            continue
        if char.isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            nums.append(num)

        elif char == "(":
            ops.append(char)
            i += 1
        elif char == ")":
            while ops[-1] != "(":
                nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
            ops.pop()
            i += 1
        elif char in ("+", "-", "*", "/"):
            while len(ops) > 0 and precedence(ops[-1]) >= precedence(char):
                nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
            ops.append(char)
            i += 1

    while len(ops) > 0:
        nums.append(operation(ops.pop(), nums.pop(), nums.pop()))

    return nums.pop()

print(calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))
