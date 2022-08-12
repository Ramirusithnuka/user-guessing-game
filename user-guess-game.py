import random
def guess(x):
    randomnumber=random.randint(1,x)
    guess=0
    while guess != randomnumber:
        guess=int(input(f'Guess a number between 1 and {x}:'))
        if guess < randomnumber:
            print("Sorry,Try again.Too low")
        elif guess > randomnumber:
            print("Sorry,Try again.Too high")
    print("Congradulations.you have guessed the number correctly")
guess(1000)