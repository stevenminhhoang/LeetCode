# O(n) space using stack
def backspaceCompare(S, T):
    stack_s, stack_t = [], []
    for char in S:
        if char == "#" and stack_s:
            stack_s.pop()
        elif char != "#":
            stack_s.append(char)

    for char in T:
        if char == "#" and stack_t:
            stack_t.pop()
        elif char != "#":
            stack_t.append(char)

    return stack_s == stack_t

print(backspaceCompare("ab#c", "ad#c"))
