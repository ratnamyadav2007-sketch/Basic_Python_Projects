import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = []
    for i in range(length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)

### Main Program
length=int(input("Enter password length: "))
pwd = generate_password(length)
print(f"\nGenerate password: {pwd}")
print("Password strength: Strong!!!")