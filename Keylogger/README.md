# 🛡️ Simple Python Keylogger

A minimal keylogger written in Python that captures all keystrokes and stores them in a log file. 

---

## ⚠️ Legal Disclaimer

This script is **strictly for educational purposes**.  
Using a keylogger on systems you do not own or have explicit permission to monitor is **illegal and unethical**.

---

## 📌 How It Works (with Example)

1. You run the script:
   ```bash
   python keylogger.py
   ```

2. It starts listening to **all keyboard inputs**.

3. While you're typing in any app — browser, notepad, terminal — the script logs each key press.

4. Suppose you typed this in any window:

   ```
   hello world123
   ```

   Then pressed:
   - `Enter`
   - `Backspace`
   - `Shift + A`

5. The `keylog.txt` file will contain something like:

   ```
   hello[Key.space]world123[Key.enter][Key.backspace]A
   ```

6. Press `ESC` to stop the keylogger.

---

## 🛠️ Installation

### 1. Install the required module:

```bash
pip install pynput
```

### 2. Run the script:

```bash
python keylogger.py
```

---

## 📝 Log Output

All captured keystrokes are saved in:
```
keylog.txt
```

Located in the same folder as the script.

---

## 💡 Tips for Learning

- Try typing different key combinations to see how they’re logged.
- Observe how special keys (e.g., `Enter`, `Shift`, `Backspace`) appear.
- Extend the project to include:
  - Timestamp for each keystroke
  - Email log every X minutes (for ethical monitoring use only)
  - Stealth mode (advanced)
  - 
---

# Build by AAKASH and RAHUL
