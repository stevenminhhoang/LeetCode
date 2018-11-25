def calculator(s):
    res = 0
    stack = []
    num = 0
    sign = "+"
    for i in range(len(s)):
        if s[i] == " ":
            continue
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        else:
            if s[i] == "(":
                stack.append(res)
                res = 0
            elif s[i] == ")":
                
            elif s[i] in ("+", "-", "*", "/"):
                if sign == "+":

                elif sign == "-":

                elif sign == "*":

                elif sign == "/":
