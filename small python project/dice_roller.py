import random

def roll_dice():
    """Rolls a dice and returns a random number from 1 to 6."""
    return random.randint(1, 6)

# MAIN PROGRAM
print("=== Welcome to dice roller ===")

while True:
    input_choice = input("Press enter to roll the dice (or 'q' to quit): ")
    
    if input_choice.lower() == 'q':
        print("Thanks for playing! Goodbye")
        break

    result = roll_dice()
    print(f"You rolled: {result}\n")