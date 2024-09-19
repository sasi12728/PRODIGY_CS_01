def encrypt(message, shift):
    """Encrypts a message using the Caesar Cipher algorithm."""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            encrypted_message += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, shift):
    """Decrypts a message encrypted with the Caesar Cipher algorithm."""
    return encrypt(encrypted_message, -shift)

def main():
    """Main function to handle user input and output."""
    print("Caesar Cipher Program")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

