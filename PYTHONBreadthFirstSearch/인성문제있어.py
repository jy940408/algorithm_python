from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

testCase = int(input())

for i in range(testCase):
    height, width, obstacle, power, startHeight, startWidth, goalHeight, goalWidth = map(int, (input()).split())
    
    board = [[0 for i in range(width)] for i in range(height)]
    visitList = [[False for i in range(width)] for i in range(height)]

    for i in range(obstacle):
        subHeight, subWidth, subLength = map(int, (input()).split())
        board[subHeight-1][subWidth-1] = subLength

    bfsDeque = deque()
    bfsDeque.append([(startHeight-1), (startWidth-1), power])

    resultCheck = False
    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        if thisDeque[2] == 0:
            break

        for i in range(4):
            subHeight = (thisDeque[0] + upDown[i])
            subWidth = (thisDeque[1] + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if not visitList[subHeight][subWidth]:
                    if board[thisDeque[0]][thisDeque[1]] >= board[subHeight][subWidth]:
                        visitList[subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2] - 1)])

                        if subHeight == (goalHeight - 1) and subWidth == (goalWidth - 1):
                            resultCheck = True
                            break

                    else:
                        if thisDeque[2] >= (board[subHeight][subWidth] - board[thisDeque[0]][thisDeque[1]]):
                            bfsDeque.append([subHeight, subWidth, (thisDeque[2] - 1)])

                            if subHeight == (goalHeight - 1) and subWidth == (goalWidth - 1):
                                resultCheck = True
                                break

        if resultCheck:
            break

    if resultCheck:
        print("잘했어!!")
    else:
        print("인성 문제있어??")