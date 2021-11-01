import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, visitList):

    visitList[heightRoot][widthRoot] = True
   
    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if  board[subHeight][subWidth] == "#" and not visitList[subHeight][subWidth]:
                 dfs(subHeight, subWidth, visitList)

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]

roundNum = int(input())

for i in range(roundNum):
    firstLine = (input()).split()
    height = int(firstLine[0])
    width = int(firstLine[1])
    board = [["0" for i in range(width)] for i in range(height)]
    visitList = [[False for i in range(width)] for i in range(height)]
    for j in range(height):
        secondLine = input()
        for k in range(width):
            board[j][k] = secondLine[k]    
    result = 0
    for j in range(height):
        for k in range(width):
            if board[j][k] == "#" and not visitList[j][k]:
                result += 1
                dfs(j, k, visitList)    
    print(result)
