gateNum, friendNum = map(int, (input()).split())

board = []
for i in range(gateNum):
    board.append(int(input()))

board = sorted(board)

start, mid, last = board[0], 0, (board[(gateNum-1)]*friendNum)
result = 0
while start <= last:

    mid = (start + last)//2

    subResult = 0
    for i in range(gateNum):
        subResult += mid//board[i]

        if subResult >= friendNum:
            break

    if subResult >= friendNum:
        result = mid
        last = mid - 1
    else:
        start = mid + 1

print(result)