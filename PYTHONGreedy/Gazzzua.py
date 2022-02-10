coinNum = int(input())
board = list(map(int, (input()).split()))

sumNum = 0
result = 0
subResult = 0
maxNum = max(board)
for i in range(coinNum):
    if board[i] < maxNum:
        subResult += board[i]
        sumNum += 1
    else:
        result += (maxNum*sumNum - subResult)
        if i != (coinNum-1):
            maxNum = max(board[i+1:])
        sumNum = 0
        subResult = 0

print(result)