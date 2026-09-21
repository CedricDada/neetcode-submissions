class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        dp = [[ '' for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)) : 
            dp[i][i] = s[i]
        
        for i in range(len(s)-1, -1,-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and len(dp[i+1][j-1]) == j-i-1:
                        dp[i][j] = s[i] + dp[i+1][j-1] + s[j]
                else:
                    if len(dp[i+1][j]) >= len(dp[i][j-1]):
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = dp[i][j-1]

        return dp[0][len(s)-1]