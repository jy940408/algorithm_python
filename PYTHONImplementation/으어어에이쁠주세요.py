length = int(input())
orderList = list(input())

board = [[["", "D"] for i in range(length)] for i in range(length)]
zombieBoard = [[0 for i in range(length)] for i in range(length)]
zombieList = []
for i in range(length):
    firstLine = input()
    for j in range(length):
        board[i][j][0] = firstLine[j]

        if board[i][j][0] == "Z":
            zombieBoard[i][j] += 1
            zombieList.append([i, j, 0])

upDown = [1, 0, -1, 0, -1, -1, 1, 1]
leftRight = [0, 1, 0, -1, -1, 1, -1, 1]

thisLocation = [0, 0, 0]
resultCheck = True
for i in orderList:
    if i == "F":
        subUpDown = (thisLocation[0] + upDown[thisLocation[2]])
        subLeftRight = (thisLocation[1] + leftRight[thisLocation[2]])

        if 0 <= subUpDown < length and 0 <= subLeftRight < length:
            thisLocation[0] = subUpDown
            thisLocation[1] = subLeftRight

            if board[thisLocation[0]][thisLocation[1]][0] == "S":
                board[thisLocation[0]][thisLocation[1]][1] = "B"

                for j in range(8):
                    lightUpDown = (thisLocation[0] + upDown[j])
                    lightLeftRight = (thisLocation[1] + leftRight[j])

                    if 0 <= lightUpDown < length and 0 <= lightLeftRight < length:
                        board[lightUpDown][lightLeftRight][1] = "B"
            
            if zombieBoard[thisLocation[0]][thisLocation[1]] != 0:
                if board[thisLocation[0]][thisLocation[1]][1] == "D":
                    resultCheck = False
                    break

    elif i == "L":
        if thisLocation[2] == 3:
            thisLocation[2] = 0
        else:
            thisLocation[2] += 1
    elif i == "R":
        if thisLocation[2] == 0:
            thisLocation[2] = 3
        else:
            thisLocation[2] -= 1

    for j in range(len(zombieList)):
        zombieUpDown = (zombieList[j][0] + upDown[zombieList[j][2]])

        if 0 <= zombieUpDown < length:
            zombieBoard[zombieList[j][0]][zombieList[j][1]] -= 1
            zombieList[j][0] = zombieUpDown
            zombieBoard[zombieList[j][0]][zombieList[j][1]] += 1

            if zombieBoard[thisLocation[0]][thisLocation[1]] != 0:
                if board[thisLocation[0]][thisLocation[1]][1] == "D":
                    resultCheck = False
                    break

        else:
            if zombieList[j][2] == 0:
                zombieList[j][2] = 2
            else:
                zombieList[j][2] = 0
    
    if not resultCheck:
        break
    
if resultCheck:
    print("Phew...")
else:
    print("Aaaaaah!")