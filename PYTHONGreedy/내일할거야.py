workNum = int(input())

board = [[0, 0] for i in range(workNum)]
for i in range(workNum):
    subjectNum, endNum = map(int, input().split())
    board[i][0], board[i][1] = subjectNum, endNum

board = sorted(board, key = lambda x: x[1], reverse = True)

resultCheck = True
thisDay = board[0][1]
for i in range(workNum):
    
    if board[i][1] <= thisDay:
        thisDay = (board[i][1] - board[i][0])
    else:
        thisDay -= board[i][0]

if thisDay >= 0:
    print(thisDay)
else:
    print(-1)