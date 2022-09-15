import random

random_number = random.randrange(1, 11)
for i in range(3):
  guess = int(input("Guess a number between 1 and 10: "))
  if guess == random_number:
    print("correct!")
    correct = True
    break
  elif guess < random_number:
    print("Too Low")
    correct = False
  elif guess > random_number:
    print("Too High")
    correct = False
if correct != True:
  print("You suck at guessing :(")
  