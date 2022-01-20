allNum = int(input())

board = [0 for i in range(allNum)]
for i in range(allNum):
    board[i] = int(input())

board = sorted(board)

result = 0
if board[0] != 1:
    result += (board[0]-1)
    board[0] = 1

for i in range(1, allNum):
    if board[i-1] < board[i]:
        result += board[i] - (board[i-1]+1)
        board[i] = board[i-1]+1

print(result)
