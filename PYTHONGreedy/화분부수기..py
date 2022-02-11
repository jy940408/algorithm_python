potNum = int(input())

result = 0
board = [False for i in range(1000001)]
for i in range(potNum):
    subBoard = list(map(int, input().split()))
    if not board[subBoard[0]] and not board[subBoard[1]] and not board[subBoard[2]]:
        result += 1

    board[subBoard[0]], board[subBoard[1]], board[subBoard[2]] = True, True, True 

print(result)
