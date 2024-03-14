import random
import string

def generate_password(length):
    # Define the set of characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a 12-character password
password_length = 12
password = generate_password(password_length)
print(f"Generated Password: {password}")