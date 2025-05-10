# Password Generator Tool

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Secure Password Generator")
try:
    length = int(input("Enter desired password length (default is 12): ") or 12)
    password = generate_password(length)
    print(f"Generated password: {password}")
except ValueError:
    print("Please enter a valid number.")
