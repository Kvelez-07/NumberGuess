import random

def supposition():
    random_number = random.randint(0,10)
    guess = int(input("Guess the secret number: "))
    tries = 5

    while tries > 0 and guess != random_number:
        tries -= 1
        if guess < random_number:
            print("Too low")
            guess = int(input("Guess the secret number: "))
        elif guess > random_number:
            print("Too high")
            guess = int(input("Guess the secret number: "))
    if guess == random_number:
            print("You guessed it right!")
            print(f"The number was: {random_number}")
    else:
        print("Syntax error.")

supposition()