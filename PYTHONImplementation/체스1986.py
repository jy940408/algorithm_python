knightUpDown = [-1, -2, -2, -1, 1, 2, 2, 1]
knightLeftRight = [-2, -1, 1, 2, -2, -1, 1, 2]

queenUpDown = [-1, -1, -1, 0, 0, 1, 1, 1]
queenLeftRight = [-1, 0, 1, -1, 1, -1, 0, 1]

height, width = map(int, input().split())

firstLine = list(map(int, input().split()))
secondLine = list(map(int, input().split()))
thirdLine = list(map(int, input().split()))
board = [["" for i in range(width)] for i in range(height)]

for i in range(firstLine[0]):
    board[firstLine[1+(i*2)]-1][firstLine[2+(i*2)]-1] = "Q"
for i in range(secondLine[0]):
    board[secondLine[1+(i*2)]-1][secondLine[2+(i*2)]-1] = "K"
for i in range(thirdLine[0]):
    board[thirdLine[1+(i*2)]-1][thirdLine[2+(i*2)]-1] = "P"

for i in range(height):
    for j in range(width):

        if board[i][j] == "Q":
            for k in range(8):
                for l in range(1, 1001):
                    if 0 <= (i+(queenUpDown[k]*l)) < height and 0 <= (j+(queenLeftRight[k]*l)) < width:
                        if board[(i+(queenUpDown[k]*l))][(j+(queenLeftRight[k]*l))] == "" or board[(i+(queenUpDown[k]*l))][(j+(queenLeftRight[k]*l))] == "V":
                            board[(i+(queenUpDown[k]*l))][(j+(queenLeftRight[k]*l))] = "V"
                        else:
                            break
                    else:
                        break

        elif board[i][j] == "K":
            for k in range(8):
                if 0 <= i+knightUpDown[k] < height and 0 <= j+knightLeftRight[k] < width:
                    if board[i+knightUpDown[k]][j+knightLeftRight[k]] == "" or board[i+knightUpDown[k]][j+knightLeftRight[k]] == "V":
                        board[i+knightUpDown[k]][j+knightLeftRight[k]] = "V"

result = 0
for i in range(height):
    for j in range(width):
        if board[i][j] == "":
            result += 1

print(result)
