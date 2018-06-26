def backspace_compare(S, T):
    stack_s, stack_t = [], []
    for char in S:
        if char == '#' and len(stack_s) > 0:
            stack_s.pop()
        elif stack_s:
            stack_s.append(char)
    for char in T:
        if char == '#' and len(stack_t) > 0:
            stack_t.pop()
        elif stack_t:
            stack_t.append(char)

    return stack_s == stack_t

# O(N) time O(1) space
