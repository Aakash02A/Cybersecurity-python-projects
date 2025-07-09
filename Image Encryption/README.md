# XOR Image Encryption/Decryption Tool 🔐🖼️

A simple Python-based tool to encrypt or decrypt image files using XOR bitwise operation. This is useful for understanding basic cryptographic principles, specifically symmetric encryption using XOR.

---

## 📌 How It Works

This tool reads an image file as raw binary data (`bytearray`), applies the XOR operation on each byte using a user-defined key (0–255), and saves the encrypted/decrypted result.

Since XOR is symmetric:
> **(Encrypted Data ⊕ Key = Original Data)**  
> **(Original Data ⊕ Key = Encrypted Data)**

Running the tool again with the same key will decrypt the image.

---

## 🧰 Features

- XOR-based symmetric encryption and decryption.
- Works with any binary file (JPG, PNG, etc.).
- Minimal and beginner-friendly.
- CLI-based tool, portable and no external dependencies.

---

## 📁 Folder Structure

```
XOR_Image_Encryptor/
│
├── xor_image_encryptor.py     # Main Python script
└── README.md                  # Documentation
```

---

## ▶️ Usage

### 1. **Run the Script**

```bash
python xor_image_encryptor.py
```

### 2. **Follow the Prompts**

```text
Image Encryption/Decryption Tool
Enter image path: input.jpg
Enter output file path: output.jpg
Enter a secret key (0-255): 123
```

The output image will be saved to the specified path.

---

## 🧪 Example

```bash
# Encrypt
Enter image path: secret.jpg
Enter output file path: encrypted.jpg
Enter a secret key (0-255): 77

# Decrypt
Enter image path: encrypted.jpg
Enter output file path: decrypted.jpg
Enter a secret key (0-255): 77
```

`decrypted.jpg` should be visually identical to `secret.jpg`.

---

## ⚠️ Notes

- Key must be an integer between `0` and `255`.  
- Both encryption and decryption use the **same function**.
- Ensure file paths are valid and accessible.

---

## 📚 Concepts Used

- **Byte-level file handling**
- **XOR (`^`) operation**
- **Symmetric encryption logic**
- **Error handling with `try-except`**

---

## 🔐 Educational Use Only

This tool is **not secure for real-world encryption**. XOR with a single key is trivially breakable. It's intended for **educational** use only to understand basic encryption.

---

# Build by AAKASH
