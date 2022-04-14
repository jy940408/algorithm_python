houseNum = int(input())

board = [[0 for i in range(3)] for i in range(houseNum)]
for i in range(houseNum):
    priceList = list(map(int, input().split()))

    if i == 0:
        board[0] = priceList
    else:
        for j in range(3):
            subResult = 0
            for k in range(3):
                if j != k:
                    if subResult == 0:
                        subResult = (priceList[j] + board[i-1][k])
                    else:
                        board[i][j] = min(subResult, (priceList[j] + board[i-1][k]))

print(min(board[houseNum-1]))