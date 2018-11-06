def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
        maxlen = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    maxlen = max(maxlen, dp[i][j])

        return maxlen
