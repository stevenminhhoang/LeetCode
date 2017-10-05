def isValid(s):
    stack = []
    d = {"]":"[", "}":"{", ")":"("}
    # print(d[")"])
    for char in s:
        if char in d.values():
            stack.append(char)
        elif char in d.keys():
            if not stack or d[char] != stack.pop():
                return False
        else:
            return False
    return stack == []
