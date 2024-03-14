import random
import string

def generate_custom_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_punctuation=True):
    # Build the set of characters to use
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    # Generate a random password with the specified conditions
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example of generating a custom password
password_length = 10
password = generate_custom_password(password_length, use_uppercase=True, use_lowercase=False, use_digits=True, use_punctuation=False)
print(f"Generated Password: {password}")