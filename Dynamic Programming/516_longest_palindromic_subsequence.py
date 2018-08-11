def longest_palindromic_subsequence(s):
    dp = [[0 for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    
