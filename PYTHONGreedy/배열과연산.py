length, sumNum = map(int, input().split())

board = list(map(int, input().split()))
board = sorted(board)
resultBoard = [i for i in range(1, length+1)]

for i in board:
    if i in resultBoard:
        resultBoard.remove(i)

    else:
        check = False
        nowNum = i

        while True:
            nowNum += sumNum

            if nowNum in resultBoard:
                check = True
                break

            if nowNum > max(resultBoard):
                break

        if check:
            resultBoard.remove(nowNum)

if resultBoard:
    print(0)
else:
    print(1)