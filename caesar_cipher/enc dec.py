# Caesar Cipher Encryption/Decryption

def encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces/symbols as is
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (0-25): ")) % 26
    except ValueError:
        print("Shift must be a number.")
        return

    if choice == 'encrypt':
        print("Encrypted message:", encrypt(message, shift))
    else:
        print("Decrypted message:", decrypt(message, shift))

if __name__ == '__main__':
    main()
