from collections import deque

def bfs(floorRoot, heightRoot, widthRoot, visitList):
    global result, resultCheck

    bfsDeque = deque()
    bfsDeque.append([floorRoot, heightRoot, widthRoot, 0])

    while bfsDeque:
        thisDeque = bfsDeque.popleft()
        thisFloor = thisDeque[0]
        thisHeight = thisDeque[1]
        thisWidth = thisDeque[2]

        for i in range(6):
            subFloor = (thisFloor + topBottom[i])
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            if 0 <= subFloor < floor and 0 <= subHeight < height and 0 <= subWidth < width:
                if not visitList[subFloor][subHeight][subWidth] and board[subFloor][subHeight][subWidth] != "#":
                    if board[subFloor][subHeight][subWidth] == "E":
                        result = (thisDeque[3] + 1)
                        resultCheck = True
                        return
                    visitList[subFloor][subHeight][subWidth] = True
                    bfsDeque.append([subFloor, subHeight, subWidth, (thisDeque[3] + 1)])

upDown = [-1, 1, 0, 0, 0, 0]
leftRight = [0, 0, -1, 1, 0, 0]
topBottom = [0, 0, 0, 0, -1, 1]

result = 0
resultCheck = False

firstLine = ""
while firstLine != "0 0 0":

    result = 0
    resultCheck = False

    firstLine = (input())
    floor, height, width = map(int, firstLine.split())
    board = [[["" for i in range(width)] for i in range(height)] for i in range(floor)]
    visitList = [[[False for i in range(width)] for i in range(height)] for i in range(floor)]

    startHeight = 0
    startWidth = 0
    startFloor = 0

    for i in range(floor):
        for j in range(height):
            secondLine = input()
            for k in range(width):
                board[i][j][k] = secondLine[k]
                if board[i][j][k] == "S":
                    startFloor = i
                    startHeight = j
                    startWidth = k
        input()

    bfs(startFloor, startHeight, startWidth, visitList)

    if firstLine != "0 0 0":
        if resultCheck:
            print("Escaped in " + str(result) + " minute(s).")
        else:
            print("Trapped!")
