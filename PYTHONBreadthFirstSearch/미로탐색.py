from queue import Queue
import sys
sys.setrecursionlimit(10**6)

def bfs(root, board, visitList):

    global resultBoard

    visitList[root[0]][root[1]] = True
    bfsQueue = Queue()
    bfsQueue.put(root)

    while not bfsQueue.empty():

        subRoot = bfsQueue.get()
        for i in range(4):
            subHeight = (subRoot[0] + upDown[i])
            subWidth = (subRoot[1] + leftRight[i])
            
            if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
                if board[subHeight][subWidth] == 1 and not visitList[subHeight][subWidth]:
                    visitList[subHeight][subWidth] = True
                    bfsQueue.put([subHeight, subWidth])
                    resultBoard[subHeight][subWidth] = resultBoard[subRoot[0]][subRoot[1]] + 1

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]

firstLine = (input()).split()
width = int(firstLine[1])
height = int(firstLine[0])

resultBoard = [[0 for i in range(width)] for i in range(height)]
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

for i in range(height):
    secondLine = input()
    for j in range(width):
        board[i][j] = int(secondLine[j])
        resultBoard[i][j] = board[i][j]

bfs([0,0], board, visitList)

print(resultBoard[height-1][width-1])
