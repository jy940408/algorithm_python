from queue import Queue

def bfs(heightRoot, widthRoot, firstVisit, secondVisit):
    bfsQueue = Queue()
    bfsQueue.put([heightRoot, widthRoot, 0, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisHeight = thisQueue[0]
        thisWidth = thisQueue[1]

        for i in range(4):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])
 
            if 0 <= subHeight < height and 0 <= subWidth < width:
                if thisQueue[2] == 0:
                    if firstVisit[subHeight][subWidth] == 0:
                        if board[subHeight][subWidth] == 0:
                            firstVisit[subHeight][subWidth] = (thisQueue[3]+1)
                            bfsQueue.put([subHeight, subWidth, 0, (thisQueue[3]+1)])
                        elif board[subHeight][subWidth] == 2:
                            firstVisit[subHeight][subWidth] = (thisQueue[3]+1)
                            bfsQueue.put([subHeight, subWidth, 1, (thisQueue[3]+1)])
                else:
                    if secondVisit[subHeight][subWidth] == 0:
                        secondVisit[subHeight][subWidth] = (thisQueue[3]+1)
                        bfsQueue.put([subHeight, subWidth, 1, (thisQueue[3]+1)])

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]        

height, width, maxTime = map(int, (input()).split())
board = [[0 for i in range(width)] for i in range(height)]
firstVisit = [[0 for i in range(width)] for i in range(height)]
secondVisit = [[0 for i in range(width)] for i in range(height)]

for i in range(height):
    firstLine = (input()).split()
    for j in range(width):
        board[i][j] = int(firstLine[j])

bfs(0 ,0, firstVisit, secondVisit)

if firstVisit[(height-1)][(width-1)] == 0 and secondVisit[(height-1)][(width-1)] == 0:
    print("Fail")
else:
    if firstVisit[(height-1)][(width-1)] == 0:
        if secondVisit[(height-1)][(width-1)] <= maxTime:
            print(secondVisit[(height-1)][(width-1)])
        else:
            print("Fail")
    elif secondVisit[(height-1)][(width-1)] == 0:
        if firstVisit[(height-1)][(width-1)] <= maxTime:
            print(firstVisit[(height-1)][(width-1)])
        else:
            print("Fail")
    else:
        result = min(firstVisit[(height-1)][(width-1)], secondVisit[(height-1)][(width-1)])
        if result <= maxTime:
            print(result)
        else:
            print("Fail")