import re
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset to default after each print

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak", Fore.RED + "🔴 Weak"
    elif score == 3 or score == 4:
        return "Medium", Fore.YELLOW + "🟠 Medium"
    else:
        return "Strong", Fore.GREEN + "🟢 Strong"

def main():
    print(Fore.CYAN + "🔐 Password Strength Checker\n")
    pwd = input("Enter your password: ")
    level, colored_output = check_password_strength(pwd)
    print(f"\nPassword Strength: {colored_output}")

if __name__ == "__main__":
    main()