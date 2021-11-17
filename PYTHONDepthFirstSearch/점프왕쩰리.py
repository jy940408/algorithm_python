import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board):
    global result

    visitList[heightRoot][widthRoot] = True

    if not result:
        for i in range(2):
            subHeight = (heightRoot + (down[i]*board[heightRoot][widthRoot]))
            subWidth = (widthRoot + (right[i]*board[heightRoot][widthRoot]))
            
            if 0 <= subHeight < length and 0 <= subWidth < length:
                if not visitList[subHeight][subWidth]:
                    if board[subHeight][subWidth] == -1:
                        result = True
                        return
                    else:
                        dfs(subHeight, subWidth, board)
    else:
        return

result = False
down = [1,0]
right = [0,1]

length = int(sys.stdin.readline())
board = []
visitList = [[False for i in range(length)] for i in range(length)]
for i in range(length):
    board.append(list(map(int, (sys.stdin.readline()).split())))

dfs(0, 0, board)

if result:
    sys.stdout.write("HaruHaru")
else:
    sys.stdout.write("Hing")

