from queue import Queue
import sys

def bfs(startRoot, visitList):
    global result, board
    
    bfsQueue = Queue()
    bfsQueue.put([startRoot[0], startRoot[1], 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisHeight = thisQueue[0]
        thisWidth = thisQueue[1]
        
        board[thisHeight][thisWidth] = thisQueue[2]

        for i in range(8):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            if 1 <= subHeight < (length+1) and 1 <= subWidth < (length+1):
                if not visitList[subHeight][subWidth]:
                    visitList[subHeight][subWidth] = True
                    bfsQueue.put([subHeight, subWidth, (thisQueue[2] +1)])

upDown = [-1, -2, -2, -1, 1, 2, 2, 1]
leftRight = [-2, -1, 1, 2, -2, -1, 1, 2]

result = ""

length, goalNum = map(int, (sys.stdin.readline()).split())
startHeight, startWidth = map(int, (sys.stdin.readline()).split())
board = [[0 for i in range(length+1)] for i in range(length+1)]
visitList = [[False for i in range(length+1)] for i in range(length+1)]

bfs([startHeight, startWidth], visitList)

for i in range(goalNum):
    goalHeight, goalWidth = map(int, (sys.stdin.readline()).split())
    result += (str(board[goalHeight][goalWidth]) + " ")
    

print(result)