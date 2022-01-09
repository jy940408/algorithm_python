def listSplit(idxList, leng):
    return [idxList[i : i+leng] for i in range(0, len(idxList), leng)]

allBook, moveBook = map(int, (input()).split())

firstLine = (input()).split()
bookList = [[], []]
for i in range(allBook):
    if int(firstLine[i]) < 0:
        bookList[0].append(int(firstLine[i])*-1)
    else:
        bookList[1].append(int(firstLine[i]))
bookList[0].sort(reverse=True)
bookList[1].sort(reverse=True)

result, rightMax, leftMax = 0, 0, 0

leftList = listSplit(bookList[0], moveBook)
for i in range(len(leftList)):
    result += leftList[i][0]*2
    leftMax = max(leftMax, leftList[i][0])

rightList = listSplit(bookList[1], moveBook)
for i in range(len(rightList)):
    result += rightList[i][0]*2
    rightMax = max(rightMax, rightList[i][0])
    
if leftMax <= rightMax:
    result -= rightMax
else:
    result -= leftMax

print(result)