firstLine = input().split()
originBoard = [0]
for i in range(24):
    originBoard.append(int(firstLine[i]))
  
turnOrder = [[[1, 24], [3, 22], [5, 1], [7, 3], [9, 5], [11, 7],  [22, 11],  [24, 9]],
             [[1, 5], [3, 7], [5, 9], [7, 11], [9, 24], [11, 22], [22, 3], [24, 1]],
             [[2, 6], [4, 8], [6, 10], [8, 12], [10, 23], [12, 21], [21, 4], [23, 2]],
             [[2, 23], [4, 21], [6, 2], [8, 4], [10, 6], [12, 8], [21, 12], [23, 10]],
             [[13, 5], [14, 6], [5, 17], [6, 18], [17, 21], [18, 22], [21, 13], [22, 14]],
             [[13, 21], [14, 22], [5, 13], [6, 14], [17, 5], [18, 6], [21, 17], [22, 18]],
             [[15, 23], [16, 24], [7, 15], [8, 16], [19, 7], [20, 8], [23, 19], [24, 20]],
             [[15, 7], [16, 8], [7, 19], [8, 20], [19, 23], [20, 24], [23, 15], [24, 16]],
             [[3, 17], [4, 19],  [17, 10], [19, 9], [10, 16], [9, 14], [16, 3], [14, 4]],
             [[3, 16], [4, 14], [17, 3], [19, 4], [10, 17], [9, 19], [16, 10], [14, 9]],
             [[1, 18], [2, 20], [18, 12], [20, 11], [12, 15], [11, 13], [15, 1], [13, 2]],
             [[1, 15], [2, 13], [18, 1], [20, 2], [12, 18], [11, 20], [15, 12], [13, 11]]]

resultCheck = True
for i in range(12):
    resultCheck = True
    subBoard = [0 for i in range(25)]

    for j in range(25):
        subBoard[j] = originBoard[j]

    for j in range(8):
        subBoard[turnOrder[i][j][0]] = originBoard[turnOrder[i][j][1]]

    for j in range(6):
        checkNum = subBoard[1+(j*4)]
        for k in range(1, 5):
            if checkNum != subBoard[k + (j*4)]:
                resultCheck = False
                break

        if not resultCheck:
            break

    if resultCheck:
        break

if resultCheck:
  print(1)
else:
  print(0)