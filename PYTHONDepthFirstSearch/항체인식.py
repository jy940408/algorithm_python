import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, mainBoard, subBoard, visitList):
    global result
    visitList[heightRoot][widthRoot] = True
    
    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if mainBoard[heightRoot][widthRoot] == mainBoard[subHeight][subWidth] and not visitList[subHeight][subWidth]:
                if subBoard[heightRoot][widthRoot] == subBoard[subHeight][subWidth] and not visitList[subHeight][subWidth]:
                    dfs(subHeight, subWidth, mainBoard, subBoard, visitList)
                else:
                    result = "NO"
                    return

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
result = ""

firstLine = (input()).split()
height = int(firstLine[0])
width = int(firstLine[1])

mainBoard = [[0 for i in range(width)] for i in range(height)]
subBoard = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

for i in range(height):
    secondLine = (input()).split()
    for j in range(width):
        mainBoard[i][j] = int(secondLine[j])

for i in range(height):
    secondLine = (input()).split()
    for j in range(width):
        subBoard[i][j] = int(secondLine[j])

changeCheck = 0
for i in range(height):
    for j in range(width):
        if result == "" and changeCheck < 2:
            if not visitList[i][j]:
                if mainBoard[i][j] != subBoard[i][j]:
                    changeCheck += 1
                    dfs(i, j, mainBoard, subBoard, visitList)
        else:
            break

if result == "NO" or changeCheck >= 2:
    print("NO")
else:
    print("YES")
