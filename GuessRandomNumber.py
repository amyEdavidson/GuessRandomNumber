import random

#declare x to be a random number between 1 and 100
x =  random.randint(1,100)
print("Guess a number between 1-100. Please provide a number: ")
#create inputs and convert string to int
guess = input()
guess = int(guess)
#game will continue until x equals user's guess
while x != guess:
    if x > guess:
        print("higher")
        guess = input()
        guess = int(guess)
    else:
        print("lower")
        guess = input()
        guess = int(guess)

print("You got it. The number was", x)