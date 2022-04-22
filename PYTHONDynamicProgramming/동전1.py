coinNum, goalNum = map(int, input().split())

board = [0 for i in range(goalNum+1)]
board[0] = 1
for i in range(coinNum):
    thisCoin = int(input())

    for j in range(1,  goalNum+1):

        if (j-thisCoin) >= 0:
            board[j] += board[j-thisCoin]

print(board[goalNum])