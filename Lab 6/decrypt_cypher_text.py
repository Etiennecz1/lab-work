# def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
def decrypt_cypher_text(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isupper():
            decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
            decrypted_text += decrypted_char
        elif char.islower():
            decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text
encrypted_text = "Uifsf jt b tfdsfu dpef!"  
key = 1
decrypted_text = decrypt_cypher_text(encrypted_text, key)
print(f"Decrypted text: {decrypted_text}")

#     return decrypted_text