#greedy,doesnt work
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(text1) and j < len(text2):
            if text1[i] == text2[j]:
                count += 1
                i += 1
                j += 1
            else:
                if len(text1) < len(text2):
                    j += 1
                else: 
                    i += 1
        return count
#2d dp
  class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)] 

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text2[j] == text1[i]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]

#2D dp with O(n) memory
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        
        next_row = [0] * (len(text2) + 1)
        
        for i in range(len(text1) - 1, -1, -1):
            curr = [0] * (len(text2) + 1)
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + next_row[j + 1]
                else:
                    curr[j] = max(curr[j + 1], next_row[j])
            next_row = curr
        
        return next_row[0]
