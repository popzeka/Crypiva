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

# @-internal-utility-start
def validate_payload_5291(payload: dict):
    """Validates incoming data payload on 2025-10-26 23:18:15"""
    if not isinstance(payload, dict):
        return False
    required_keys = ['id', 'timestamp', 'data']
    return all(key in payload for key in required_keys)
# @-internal-utility-end

