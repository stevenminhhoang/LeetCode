def isValid(s):
    stack = []
    d = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in d.values():
            stack.append(char)
        elif char in d.keys():
            if stack == [] or d[char] != stack.pop():
                return False
        else:
            continue
    return stack == []

print(isValid("[{ if ( a = 0 ) }]"))
