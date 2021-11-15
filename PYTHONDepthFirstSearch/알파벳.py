import sys

def dfs(heightRoot, widthRoot, board, visitList, visitDict, subResult):

    global result

    result = max(result, subResult)

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if not visitList[subHeight][subWidth]:
                visitList[subHeight][subWidth] = True
                if visitDict[ord(board[subHeight][subWidth])-65] != 1:
                    visitDict[ord(board[subHeight][subWidth])-65] = 1

                    dfs(subHeight, subWidth, board, visitList, visitDict, subResult+1)

                    visitDict[ord(board[subHeight][subWidth])-65] = 0
                visitList[subHeight][subWidth] = False

result = 0
upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]

height, width = map(int, (sys.stdin.readline()).split())
board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]
visitDict = [0 for i in range(26)]

for i in range(height):
    firstLine = sys.stdin.readline()
    for j in range(width):
        board[i][j] = firstLine[j]

visitDict[ord(board[0][0])-65] = 1
dfs(0, 0, board, visitList, visitDict, 1)

print(result)