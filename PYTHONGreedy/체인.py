roundNum = int(input())
board = list(map(int, input().split()))
board.sort()

subResult = 0
result = 0
for i in range(roundNum):
    thisCount = roundNum-i-1
    
    subResult += board[i]
    if subResult >= thisCount:
        result = thisCount
        break

print(result)