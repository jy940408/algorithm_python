testNum = int(input())

board = [[0 for i in range(10)] for i in range(testNum + 1)]

for i in range(1, 10):
    board[1][i] = 1

for i in range(2, (testNum + 1)):
    board[i][0] = board[i - 1][1]
    board[i][9] = board[i - 1][8]

    for j in range(1, 9):
        board[i][j] = (board[i-1][j-1] + board[i-1][j+1])

result = 0
for i in range(10):
    result += board[testNum][i]

print(result%1000000000)