import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList):
    global result
    visitList[heightRoot][widthRoot] = True

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if not visitList[subHeight][subWidth] and board[subHeight][subWidth] != "X":
                if board[subHeight][subWidth] == "P":
                    result += 1
                dfs(subHeight, subWidth, board, visitList)


upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
result = 0

height, width = map(int, (input()).split())
board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

place = []
for i in range(height):
    secondLine = input()
    for j in range(width):
        board[i][j] = secondLine[j]
        if secondLine[j] == "I":
            place = [i, j]

dfs(place[0], place[1], board, visitList)

if result != 0:
    print(result)
else:
    print("TT")