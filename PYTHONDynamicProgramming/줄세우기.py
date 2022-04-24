roundNum = int(input())

board = [0 for i in range(roundNum)]
for i in range(roundNum):
    board[i] = int(input())

dp = [[0 for i in range(roundNum)] for i in range(roundNum)]
subResult = 0
for i in range(roundNum):
    for j in range(roundNum):
        if i == 0:
            dp[i][i] = 1
            if board[i] < board[j]:
                dp[i][j] = (dp[i][i]+1)
        
        else:
            dp[i][i] = max(dp[i-1][i], 1)
            if i <= j:
                if board[i] < board[j]:
                    dp[i][j] = max(dp[i-1][j], (dp[i][i]+1))
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
        
        subResult = max(subResult, dp[i][j])
            
print(roundNum - subResult)
                    