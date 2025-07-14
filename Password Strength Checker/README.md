# 🔐 Password Strength Checker

A simple Python CLI tool to check the strength of a password using regular expressions and color-coded output via `colorama`.

## Features

- Checks password length (minimum 8 characters)
- Detects uppercase and lowercase letters
- Verifies presence of numbers
- Detects special characters
- Color-coded strength display (Weak 🔴, Medium 🟠, Strong 🟢)

## Requirements

- Python 3.x
- `colorama` module

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/password-strength-checker.git
    cd password-strength-checker
    ```

2. **Install dependencies**:
    ```bash
    pip install colorama
    ```

## Usage

Run the script from the command line:

```bash
python password_checker.py
```

---

Then enter your password when prompted:

bash
Copy
Edit
🔐 Password Strength Checker

Enter your password: MyP@ssw0rd

Password Strength: 🟢 Strong

---

## Strength Criteria

| Score | Criteria Met               | Strength  |
| ----- | -------------------------- | --------- |
| ≤ 2   | Fewer than 3 checks passed | 🔴 Weak   |
| 3–4   | Moderate checks passed     | 🟠 Medium |
| 5     | All checks passed (secure) | 🟢 Strong |

---

# Build by AAKASH

