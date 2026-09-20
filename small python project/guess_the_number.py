import random

print("==== Welcome To The Game ====")
print("+++ I have selected a number from 1 to 100 +++")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low try again")

    elif guess > number:
        print("Too high try again")

    else:
        print("======= Congratulations!!!! You have gussed the number =======")
        print(f"You took {attempts} attempts.")
        break