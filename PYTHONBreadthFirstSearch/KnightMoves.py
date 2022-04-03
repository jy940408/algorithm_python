from collections import deque

upDown = [-1, -2, -2, -1, 1, 2, 2, 1]
leftRight = [-2, -1, 1, 2, -2, -1, 1, 2]

while True:
    try:
        firstLine = input().split()
        startHeight, startWidth = (ord(firstLine[0][0])-97), (int(firstLine[0][1])-1)
        goalHeight, goalWidth = (ord(firstLine[1][0])-97), (int(firstLine[1][1])-1)

        visitList = [[False for i in range(8)] for i in range(8)]
        bfsDeque = deque()
        bfsDeque.append([startHeight, startWidth, 0])
        while bfsDeque:
            thisDeque = bfsDeque.popleft()

            if thisDeque[0] == goalHeight and thisDeque[1] == goalWidth:
                print("To get from", firstLine[0], "to", firstLine[1], "takes", thisDeque[2], "knight moves.")
                break

            for i in range(8):
                thisHeight = (thisDeque[0] + upDown[i])
                thisWidth = (thisDeque[1] + leftRight[i])

                if 0 <= thisHeight < 8 and 0 <= thisWidth < 8:
                    if not visitList[thisHeight][thisWidth]:
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2] + 1)])

    except EOFError:
        break
