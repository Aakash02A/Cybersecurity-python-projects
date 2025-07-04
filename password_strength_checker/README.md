# 🔐 Password Strength Checker

A simple command-line Python tool to evaluate the strength of a given password.  
It checks for key security features like length, character variety, and special symbols, and provides visual feedback using color-coded strength indicators.

---

## 📌 Features

- Checks for:
  - Minimum length (8 characters)
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Returns one of the following:
  - 🔴 Weak
  - 🟠 Medium
  - 🟢 Strong
- Terminal color-coded output using `colorama`

---

## 💻 How It Works

The tool evaluates the password based on 5 key rules. For each rule satisfied, 1 point is awarded:
- Score 0-2 → Weak
- Score 3-4 → Medium
- Score 5 → Strong

Example:
```bash
Enter your password: Rahul123
Password Strength: 🟠 Medium
```
