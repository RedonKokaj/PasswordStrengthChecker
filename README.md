# Password Strength Checker

## Overview
This is a simple GUI-based **Password Strength Checker** built using Python and Tkinter. It evaluates the strength of a password based on length, variety, and entropy. Additionally, it checks if the password has been leaked in data breaches using the **Have I Been Pwned** API.

## Features
- **Password Strength Evaluation**: Uses character variety and entropy to determine if a password is *Weak, Medium, or Strong*.
- **HIBP Breach Check**: Checks if a password has been exposed in known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/).
- **User-Friendly GUI**: Built with Tkinter for a simple and intuitive user experience.

## Requirements
- Python 3.x
- `requests` library (for HIBP API queries)

To install the required library, run:
```bash
pip install requests
```

## How to Use
1. Run the script:
   ```bash
   python password_checker.py
   ```
2. Enter a password in the input field.
3. Click the **"Check Password"** button.
4. The application will:
   - Display the **password strength**.
   - Show if the password has been **leaked** in data breaches.

## Code Structure
- `calculate_entropy(password)`: Calculates password entropy based on character variety.
- `check_password_strength(password)`: Evaluates password strength based on length, variety, and entropy.
- `check_hibp(password)`: Queries the **HIBP API** to check if the password has been leaked.
- `check_password()`: Retrieves the password from the entry field and updates the GUI with results.
- `main()`: Initializes the Tkinter GUI.

## Screenshot
![Image](https://github.com/user-attachments/assets/3399c403-c458-4463-afbc-e1a45195263f)

## Notes
- The program **never sends the actual password** to the HIBP API. Instead, it uses the **first 5 characters** of the SHA-1 hash for anonymity.
- If a password appears in a breach, it is strongly recommended to **change it immediately**.

## License
This project is open-source and available under the MIT License.

