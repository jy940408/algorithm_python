from queue import Queue

def boardCheck(headHeight, headWidth, nowDirection):
    subHeight = (headHeight + upDown[nowDirection])
    subWidth = (headWidth + leftRight[nowDirection])

    if subHeight >= 0 and subWidth >= 0 and subHeight < length and subWidth < length:
        if board[subHeight][subWidth] == 0:
            return 0
        elif board[subHeight][subWidth] == 1:
            return 1
        else:
            return 2
    else:
        return 3

def turnCheck(nowDirection, orderDirection):
    if orderDirection == "L":
        if nowDirection == 0:
            return 3
        elif nowDirection == 1:
            return 0
        elif nowDirection == 2:
            return 1
        else:
            return 2
    else:
        if nowDirection == 0:
            return 1
        elif nowDirection == 1:
            return 2
        elif nowDirection == 2:
            return 3
        else:
            return 0

length = int(input())
appleNum = int(input())
board = [[0 for i in range(length)] for i in range(length)]
board[0][0] = 2

headHeight = headWidth = tailHeight = tailWidth = 0
tailQueue = Queue()
tailQueue.put([0, 0])

for i in range(appleNum):
    height, width = map(int, (input()).split())
    board[height - 1][width - 1] = 1

turnNum = int(input())
turnQueue = Queue()

for i in range(turnNum):
    firstLine = (input()).split()
    turnQueue.put([int(firstLine[0]), firstLine[1]])

nowTime = 0
nowDirection = 0
order = turnQueue.get()
orderTime = order[0]
orderDirection = order[1]

upDown = [0, 1, 0, -1]
leftRight = [1, 0, -1, 0]

resultCheck = True
while resultCheck:
    nowTime += 1

    subHeight = (headHeight + upDown[nowDirection])
    subWidth = (headWidth + leftRight[nowDirection])

    if boardCheck(headHeight, headWidth, nowDirection) == 0:
        board[subHeight][subWidth] = 2

        tail = tailQueue.get()
        tailQueue.put([subHeight, subWidth])
        tailHeight = tail[0]
        tailWidth = tail[1]
        board[tailHeight][tailWidth] = 0

        headHeight, headWidth = subHeight, subWidth
    elif boardCheck(headHeight, headWidth, nowDirection) == 1:
        board[subHeight][subWidth] = 2

        tailQueue.put([subHeight, subWidth])
        headHeight, headWidth = subHeight, subWidth
    elif boardCheck(headHeight, headWidth, nowDirection) == 2 or boardCheck(headHeight, headWidth, nowDirection) == 3:
        resultCheck = False

    if nowTime == orderTime:
        nowDirection = turnCheck(nowDirection, orderDirection)

        if (not turnQueue.empty()):
            order = turnQueue.get()
            orderTime = order[0]
            orderDirection = order[1]

print(nowTime)