# O(m * n)
def wildcard_matching(s, p):
    # replace multiple * with one *
    pattern = list(p)
    write_index = 0
    is_first = True
    for i in range(len(pattern)):
        if pattern[i] == '*':
            if is_first:
                pattern[write_index] = pattern[i]
                write_index += 1
                is_first = False
        else:
            pattern[write_index] = pattern[i]
            write_index += 1
            is_first = True

    dp = [[False for j in range(write_index + 1)] for i in range(len(s) + 1)]
    dp[0][0] = True

    if write_index > 0 and pattern[0] == '*':
        dp[0][1] = True

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if s[i - 1] == pattern[j - 1] or pattern[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = False

    return dp[-1][-1]

# print(wildcard_matching("a", "?"))




# Alternative
def is_match(s, p):
    dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
    dp[0][0] = True

    for i in range(1, len(dp[0])):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 1]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = False

    return dp[-1][-1]

print(is_match("a", "?*******"))
