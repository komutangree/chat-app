
def load_key(file_path):
    decryption_key = {}
    with open(file_path, "r") as key_file:
        for line in key_file:
            original, replacement = line.strip().split(" -> ")
            decryption_key[replacement] = original  # Reverse the mapping
    return decryption_key


def decrypt_text(encrypted_text, decryption_key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += decryption_key.get(char, char)  # Replace using the key
    return decrypted_text


to_decrypt_text = input("Enter the text to decrypt: ")
decryption_key = load_key("key.key")
decrypted_text = decrypt_text(to_decrypt_text, decryption_key)
print("Decrypted text:", decrypted_text)
