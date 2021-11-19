import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board):
    global result

    if len(result) == 6:
        resultSet.add(result)
        return

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if 0 <= subHeight < 5 and 0 <= subWidth < 5:
            result += str(board[subHeight][subWidth])
            dfs(subHeight, subWidth, board)
            result = result[:-1]

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]

result = ""
resultSet = set()

board = [[0 for i in range(5)] for i in range(5)]
for i in range(5):
    firstLine = (input()).split()
    for j in range(5):
        board[i][j] = int(firstLine[j])

for i in range(5):
    for j in range(5):
        dfs(i, j, board)

print(len(resultSet))