import random 

print("Welcome to hangman")
print("..................................")

wordDictionary = ['house', 'flat', 'room', 'coffee', 'phone', 'table', 'orange']

randomWord = random.choice(wordDictionary)

for x in randomWord:
   print("_", end=' ')

