import random

def guessing():
    print("\nThis is a guessing game, think about a number and I'll guess it for you.\n")
    tries = 8

    while True:
        random_number = random.randint(0, 17)
        supposition = f"The number is {random_number}"
        print(supposition)

        feedback = str(input("Is it too 'low' = L, 'high = H or 'correct' = C ? ")).lower()
        if feedback == "low" or feedback == "L" or feedback == "l":
            random_number+=1 #add to the random number
            tries -=1
            print(supposition)
        elif feedback == "high" or feedback == "H" or feedback == "h":
            random_number -=1 #remove from the random number
            tries -=1
            print(supposition)
        elif feedback == "correct" or feedback == "C" or feedback == "c":
            print("Correct!")
            print(f"The number is {random_number}")
            break
    if tries == 0:
        print("I lost, I'm out of tries.")

guessing()