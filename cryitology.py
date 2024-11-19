from random import randint, choice
 


to_encrypt = input("Enter text to encrypt: ")


def generate_random_character():
    categories = [
        chr(randint(65, 90)),  # Uppercase letter
        chr(randint(97, 122)),  # Lowercase letter
        chr(randint(48, 57))    # Number
    ]
    return choice(categories)

encryption_key = {}
encrypted_text = ""

for char in to_encrypt:
    if char not in encryption_key:  
        replacement = generate_random_character()
        while replacement in encryption_key.values():  
            replacement = generate_random_character()
        encryption_key[char] = replacement
    encrypted_text += encryption_key[char]


with open("key.key", "w") as key_file:
    for original, replacement in encryption_key.items():
        key_file.write(f"{original} -> {replacement}\n")


print("Encrypted text:", encrypted_text)
