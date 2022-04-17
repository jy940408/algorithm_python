roundNum, weight = map(int, input().split())

board = [[0 for i in range(weight+1)] for i in range(roundNum)]
for i in range(roundNum):
    thisWeight, thisValue = map(int, input().split())
    
    for j in range((weight+1)):
        if j >= thisWeight:
            if board[i-1][j] < (board[i-1][j-thisWeight] + thisValue):
                board[i][j] = (board[i-1][j-thisWeight] + thisValue)
            else:
                board[i][j] = board[i-1][j]
        else:
            board[i][j] = board[i-1][j]

print(max(board[roundNum-1]))