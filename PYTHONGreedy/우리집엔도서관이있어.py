import sys
bookNum = int(sys.stdin.readline())

board = [0 for i in range(bookNum)]
for i in range(bookNum):
    board[i] = int(sys.stdin.readline())

result = 0
thisBook = bookNum
for i in range(bookNum-1, -1, -1):
    if board[i] == thisBook:
        thisBook -= 1
        result += 1

print((bookNum-result))