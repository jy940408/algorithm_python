roundNum = int(input())

board = [[0 for i in range(roundNum)] for i in range(roundNum)]
for i in range(roundNum):
    numList = list(map(int, input().split()))
    for j in range(i+1):
        board[i][j] = numList[j]

    if i != 0:
        for j in range(i+1):
            if j == 0:
                board[i][j] += board[i-1][j]
            else:
                board[i][j] += max(board[i-1][j], board[i-1][j-1])
    
print(max(board[roundNum-1]))