workNum = int(input())

board = [[0, 0] for i in range(workNum)]
for i in range(workNum):
    termNum, endNum = map(int, input().split())
    board[i][0], board[i][1] = termNum, endNum

board = sorted(board, key = lambda x: (x[1], x[0]), reverse = True)

resultCheck = True
thisTime = board[0][1]
for i in range(workNum):
    
    if board[i][1] <= thisTime:
        thisTime = (board[i][1] - board[i][0])
    else:
        thisTime -= board[i][0]

if thisTime >= 0:
    print(thisTime)
else:
    print(-1)