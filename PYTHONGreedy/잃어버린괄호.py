testcase = (input()).split('-')

board = []
for i in range(len(testcase)):

    subSum = 0
    for j in range(len(testcase[i].split('+'))):
        subSum += int(testcase[i].split('+')[j])
    
    board.append(subSum)

result = board[0]
for i in range(1, len(board)):
    result -= board[i]

print(result)