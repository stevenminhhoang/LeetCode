def valid_parentheses(s):
    stack = []
    d = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char == "|":
            if stack == [] or stack[-1] != '|':
                stack.append(char)
            else:
                stack.pop()
        elif char in d.values():
            stack.append(char)
        elif char in d.keys():
            if stack == [] or d[char] != stack.pop():
                return False
        else:
            continue
    return stack == []


print(valid_parentheses("{[(|||)]}"))
# print(valid_parentheses("{}"))
