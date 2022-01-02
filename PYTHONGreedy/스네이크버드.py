fruitNum, snakebird = map(int, (input()).split())

fruitList = []
fruits = (input()).split()
for i in range(fruitNum):
    fruitList.append(int(fruits[i]))
fruitList = sorted(fruitList)

for i in range(fruitNum):
    if snakebird >= fruitList[i]:
        snakebird += 1

print(snakebird)