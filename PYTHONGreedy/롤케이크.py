cakeNum, roundNum = map(int, (input()).split())
board = list(map(int, (input()).split()))

board = sorted(board)

result = 0
checkNum = 0
resultCheck = False
for i in range(cakeNum):
    if board[i]%10 == 0:
        if (checkNum + (board[i]//10 - 1)) <= roundNum:
            result += board[i]//10
            checkNum += (board[i]//10)-1
        else:
            result += (roundNum - checkNum)
            resultCheck = True
            break

if not resultCheck:
    for i in range(cakeNum):
        if board[i]%10 != 0:
            if (checkNum + board[i]//10) <= roundNum:
                result += board[i]//10
                checkNum += (board[i]//10)
            else:
                result += (roundNum - checkNum)
                break

print(result)