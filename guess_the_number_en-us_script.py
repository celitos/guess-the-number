#Guess the number?"
import random

guessTaken = 0

print("Hello, What's your name? ")
myName = input()

number = random.randint(1,10)
print('Well ' + myName + ' I'm thinking a number between 1 to 10')

while guessTaken < 3:
    print('Guess the number??? ')
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print('too low')
    if guess  > number:
        print('too high')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessTaken)
    print('Good Job, ' + myName + ' you guessed the number in ' + guessesTaken + ' attempts ')

if guess != number:
   number = str(number)
   print('Nope, this was the number '+ number)
    
 #more updates in 1.1 version sooner
      #maybe update the directory idk :)
