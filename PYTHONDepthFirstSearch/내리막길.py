import sys
sys.setrecursionlimit(10**6)

def dfs(thisLocation):
    global result, dp

    if dp[thisLocation[0]][thisLocation[1]] != -1:
        return dp[thisLocation[0]][thisLocation[1]]

    if thisLocation[0] == (height-1) and thisLocation[1] == (width-1):
        return 1

    dp[thisLocation[0]][thisLocation[1]] = 0
    for i in range(4):
        thisHeight = thisLocation[0] + upDown[i]
        thisWidth = thisLocation[1] + leftRight[i]

        if 0 <= thisHeight < height and 0 <= thisWidth < width:
            if board[thisHeight][thisWidth] < board[thisLocation[0]][thisLocation[1]]:
                    dp[thisLocation[0]][thisLocation[1]] += dfs([thisHeight, thisWidth])
    
    return dp[thisLocation[0]][thisLocation[1]]

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

result = 0

height, width = map(int, (sys.stdin.readline()).split())

dp = [[-1 for i in range(width)] for i in range(height)]
board = [[0 for i in range(width)] for i in range(height)]
for i in range(height):
    firstLine = (sys.stdin.readline()).split()
    
    for j in range(width):
        board[i][j] = int(firstLine[j])

print(dfs([0, 0]))