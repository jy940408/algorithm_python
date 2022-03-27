roundNum, goalNum = map(int, input().split())

board = [0 for i in range(27)]
resultNum = 0

board[1] = roundNum
resultNum = roundNum

for i in range(26, 1, -1):
    thisNum = (goalNum-resultNum)//(i-1)

    if thisNum > 0:
        resultNum = (resultNum - thisNum) + (i*thisNum)
        board[1] -= thisNum
        board[i] += thisNum
    
result = ""
for i in range(27):
    if board[i] != 0:
        result += chr(i+64)*board[i]

if resultNum == goalNum and board[1] >= 0:
    print(result)
else:
    print("!")