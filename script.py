# Crypiva: Simple Password Generator

import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Generated password:", password)
