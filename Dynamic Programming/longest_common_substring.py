# O(m * n)
def longest_common_substring(A, B):
    dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    row, col = 0, 0
    length = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] == 0
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if length < dp[i][j]:
                    length = dp[i][j]
                    row = i
                    col = j
            else:
                dp[i][j] = 0

    if length == 0:
        return ""

    res = []
    while dp[row][col] != 0:
        res.append(A[row - 1])
        row -= 1
        col -= 1

    return "".join(res[::-1])

print(longest_common_substring("abcGeeksforGeeks", "xywzGeeksQuizGeeksfor"))
