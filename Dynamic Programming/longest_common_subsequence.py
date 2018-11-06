# O(m * n)
def longest_common_subsequence(A, B):
    dp = [[None for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

print(longest_common_subsequence("ABCDGH", "AEDFHR"))
print(longest_common_subsequence("AGGTAB", "GXTXAYB"))
