def diceOrder(dice, direction):
    subDice = []
    if direction == 1:
        subDice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 2:
        subDice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 3:
        subDice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direction == 4:
        subDice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    return subDice

def locationOrder(thisHeight, thisWidth, direction):
    if direction == 1:
        thisWidth += 1
    elif direction == 2:
        thisWidth -= 1
    elif direction == 3:
        thisHeight -= 1
    elif direction == 4:
        thisHeight += 1
    
    if 0 <= thisHeight < height and 0 <= thisWidth < width:
        return [thisHeight, thisWidth]
    else:
        return [-1, -1]

height, width, thisHeight, thisWidth, roundNum = map(int, (input()).split())

board = [list(map(int, (input()).split())) for i in range(height)]
orderList = list(map(int, (input()).split()))

result = ""
dice = [0, 0, 0, 0, 0, 0]
for i in range(roundNum):
    thisLocation = locationOrder(thisHeight, thisWidth, orderList[i])

    if thisLocation[0] != -1 and thisLocation[1] != -1:
        dice = diceOrder(dice, orderList[i])

        thisHeight = thisLocation[0]
        thisWidth = thisLocation[1]

        if board[thisHeight][thisWidth] == 0:
            board[thisHeight][thisWidth] = dice[5]
        else:
            dice[5] = board[thisHeight][thisWidth]
            board[thisHeight][thisWidth] = 0

        result += str(dice[0]) + "\n"

print(result)