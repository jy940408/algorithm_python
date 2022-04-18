roundNum = int(input())

for i in range(roundNum):
    coinNum = int(input())
    coinList = list(map(int, input().split()))
    goalNum = int(input())

    board = [[0 for i in range(goalNum+1)] for i in range(coinNum)]
    result = 0
    for j in range(coinNum):
        board[j][0] = 1
        for k in range(1, goalNum+1):
            board[j][k] = board[j-1][k]
            if (k-coinList[j]) >= 0:
                board[j][k] += board[j][k-coinList[j]]

    print(board[(coinNum-1)][goalNum])