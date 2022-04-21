chapterNum, timeNum = map(int, input().split())

board = [[0 for i in range(timeNum+1)] for i in range(chapterNum)]
result = 0
for i in range(chapterNum):
    thisTime, thisNum = map(int, input().split())
    
    for j in range(timeNum+1):
        if j >= thisTime:
            board[i][j] = max(board[i-1][j], (board[i-1][j-thisTime] + thisNum))
        else:
            board[i][j] = board[i-1][j]

        result = max(board[i][j], result)    

print(result)