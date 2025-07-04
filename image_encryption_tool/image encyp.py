def xor_encrypt_decrypt(input_path, output_path, key):
    try:
        with open(input_path, 'rb') as f:
            data = bytearray(f.read())  # Read image as byte array

        for i in range(len(data)):
            data[i] ^= key  # XOR each byte with key

        with open(output_path, 'wb') as f:
            f.write(data)

        print(f"[+] Process completed. Output saved to: {output_path}")
    except FileNotFoundError:
        print("[-] File not found. Please check the path.")
    except Exception as e:
        print(f"[-] Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    print("Image Encryption/Decryption Tool")
    input_file = input("Enter image path: ")
    output_file = input("Enter output file path: ")
    key = int(input("Enter a secret key (0-255): "))

    if 0 <= key <= 255:
        xor_encrypt_decrypt(input_file, output_file, key)
    else:
        print("[-] Key must be between 0 and 255.")

