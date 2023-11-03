import random

while True:
    input("Press Enter to roll the die...")
    result = random.randint(1, 6)
    print(f"The die shows: {result}")
    again = input("Roll again? (y/n): ")
    if again.lower() != 'y':
        break