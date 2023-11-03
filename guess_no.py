import random

random_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == random_number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < random_number:
        print("Try higher.")
    else:
        print("Try lower.")