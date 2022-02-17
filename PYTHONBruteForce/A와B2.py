def wordOrder(startWord, goalWord):
  global lengthCheck, result

  if result == 1 or (len(goalWord) < len(startWord)):
    return
  
  if goalWord == startWord:
    result = 1
    return

  if lengthCheck and result == 0:
    if goalWord[len(goalWord)-1] == "A":
      wordOrder(startWord, goalWord[:len(goalWord)-1])
    if goalWord[0] == "B":
      wordOrder(startWord, list(reversed(goalWord))[:len(goalWord)-1])
    
lengthCheck = True
result = 0

startWord = list(input())
goalWord = list(input())

wordOrder(startWord, goalWord)

print(result)
