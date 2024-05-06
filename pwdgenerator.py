import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    characters = string.ascii_letters
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    pwd = ''
    while len(pwd) < min_length:
        pwd += random.choice(characters)
        
    return pwd

pwd = generate_password(10)
print(pwd)
