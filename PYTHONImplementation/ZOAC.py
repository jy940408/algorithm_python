def orderWord(startIdx, board):
    if not board:
        return
    minWord = min(board)
    thisIdx = board.index(minWord)

    result[startIdx + thisIdx] = minWord
    print("".join(result))

    orderWord(startIdx + (thisIdx+1), board[thisIdx+1:])
    orderWord(startIdx, board[:thisIdx])

startWord = input()
board = []
for i in startWord:
    board.append(i)
result = ["" for i in range(len(board))]

orderWord(0, board)