from collections import deque

result = []

while True:
    greedyDeque = deque()
    count = 0
    testCase = input()

    if testCase[0] == "-":
        break

    for i in range(len(testCase)):
        if not greedyDeque and testCase[i] == '}':
            count += 1
            greedyDeque.append('{')
        elif greedyDeque and testCase[i] == '}':
            greedyDeque.pop()
        else:
            greedyDeque.append(testCase[i])

    count += len(greedyDeque)//2
    result.append(count)

for i in range(len(result)):
    print(str(i+1) + '.', result[i])