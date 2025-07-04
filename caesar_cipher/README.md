# 🛡️ Caesar Cipher Tool

A command-line utility to **encrypt** and **decrypt** messages using the Caesar Cipher algorithm. Great for learning basic cryptography, creating puzzles, or encoding secret messages within a local or collaborative environment.

---

## 🔐 What is Caesar Cipher?

Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number (shift key) of positions down the alphabet.

### Example (Shift = 3):
- A → D
- B → E
- X → A
- Z → C

> **Encryption**: Shift letters forward  
> **Decryption**: Shift letters backward

---

## 📦 Features

- Encrypt or decrypt any string using a simple shift
- Supports both uppercase and lowercase
- Leaves spaces, numbers, and punctuation unchanged
- Command-line interface for real-time usage

---

## ⚙️ Usage

### 🔧 Requirements
- Python 3.x installed

### 🏃 Run via Command Line

```bash
python caesar_cipher_tool.py <mode> <shift> "<text>"
````

* `<mode>`: `e` for encrypt, `d` for decrypt
* `<shift>`: Number of positions to shift
* `<text>`: The message to process (wrap in quotes)

---

## 🧪 Examples

### Encrypt:

```bash
python caesar_cipher_tool.py e 4 "meet at library at 5pm"
```

Output:

```
Result: qiix ex plevvex ex 5ts
```

### Decrypt:

```bash
python caesar_cipher_tool.py d 4 "qiix ex plevvex ex 5ts"
```

Output:

```
Result: meet at library at 5pm
```

---

## 💡 Real-world Scenario

You and a friend agree on a shift value (e.g., 4). You encrypt a secret note and send it. Your friend uses the same script and shift value to decrypt it.

---

## 🛠️ How It Works

The script:

1. Loops through each character in the message.
2. Applies a shift based on encryption or decryption mode.
3. Converts characters using ASCII math and wraps alphabetically using `% 26`.
4. Non-alphabet characters are preserved.

```python
chr((ord(char) - base + shift) % 26 + base)
```


* `ord(char)` – ASCII of char
* `base` – `ord('a')` or `ord('A')`
* `shift` – Provided shift value

---

## 🧑‍🎓 Author

Built by Aakash — focused on cybersecurity, scripting, and real-world learning through hands-on tools.

---


