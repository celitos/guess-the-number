#Jogo "qual o número?"
import random

guessTaken = 0

print("Olá qual o seu nome? ")
myName = input()

number = random.randint(1,10)
print('Bem ' + myName + ' Estou Pensando entre um número de 1 a 10.')

while guessTaken < 3:
    print('Adivinhe??? ')
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print('Sua tentativa é muito baixa')
    if guess  > number:
        print('Sua tentativa é muito alta')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessTaken)
    print('Bom trabalho ' + myName + ' Você acertou meu número em ' + guessesTaken + ' tentativas ')

if guess != number:
   number = str(number)
   print('Não. Alguém errou o número que era'+ number)
    
    
