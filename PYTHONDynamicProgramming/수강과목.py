import sys

timeNum, subjectNum = map(int, (sys.stdin.readline()).split())

board = [[0 for i in range(timeNum+1)] for i in range(subjectNum)]
for i in range(subjectNum):
    thisValue, thisTime = map(int, (sys.stdin.readline()).split())

    for j in range(timeNum+1):
        if j >= thisTime:
            board[i][j] = max(board[i-1][j], (board[i-1][j-thisTime] + thisValue))
        else:
            board[i][j] = board[i-1][j]

print(board[subjectNum-1][timeNum])