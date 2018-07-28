# Time complexity: equivalent to nth catalan number
def generate_parentheses(n):
    def backtrack(lis, string, open, close, max):
        if len(string) == 2 * max:
            lis.append(string)

        if open < max:
            backtrack(lis, string + "(", open + 1, close, max)
        if close < open:
            backtrack(lis, string + ")", open, close + 1, max)


    lis = []
    backtrack(lis, "", 0, 0, n)
    return lis


print(generate_parentheses(3))
