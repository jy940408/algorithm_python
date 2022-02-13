length = int(input())
board = list(map(int, (input()).split()))

divideNum = 0
minusNum = 0
for i in range(length):
    subNum = 0
    while True:
        if board[i] != 0:
            if board[i]%2 == 1:
                minusNum += 1
                board[i] -= 1
            else:
                board[i] //= 2
                subNum += 1

        if board[i] == 0:
            divideNum = max(divideNum, subNum)
            break

print((divideNum + minusNum))