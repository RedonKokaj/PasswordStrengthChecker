import hashlib
import requests
import string
import math
import tkinter as tk
from tkinter import messagebox

def calculate_entropy(password):
    #Calculate password entropy based on character variety

    character_sets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]
    
    pool_size = 0 # Pool size is the number of unique characters in the password
    for charset in character_sets:
        if any(char in charset for char in password): # Check if any character from the charset is in the password
            pool_size += len(charset) # Increase pool size if charset is used
    entropy = math.log2(pool_size) * len(password) 
    return entropy

def check_password_strength(password):
    # Check password strength based on length, variety, and entropy

    length_score = min(len(password) / 12, 1)  # Assuming a max length of 12 for full score, max 1.0
    
    variety_score = 0 # Variety score based on character types used in the password, max 1.0
    if any(char in string.ascii_lowercase for char in password):
        variety_score += 0.25
    if any(char in string.ascii_uppercase for char in password):
        variety_score += 0.25
    if any(char in string.digits for char in password):
        variety_score += 0.25
    if any(char in string.punctuation for char in password):
        variety_score += 0.25
    
    entropy_score = min(calculate_entropy(password) / 60, 1) # Assuming a max entropy of 60 for full score, max 1.0

    final_score = (length_score + variety_score + entropy_score) / 3 # Average of the three scores

    if final_score > 0.8:
        return "Strong"
    elif final_score > 0.5:
        return "Medium"
    else:
        return "Weak"

def check_hibp(password):
    # Check if a password has been leaked in data breaches using Have I Been Pwned API
    
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    # The API requires the first 5 characters of the SHA1 hash, the rest is used to check against the response
    # Example: For password "password", the SHA1 hash is "5BAA61E4" and we need to send "5BAA6"
    first5 = sha1_password[:5] 
    rest = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{first5}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        return "Error checking HIBP API"

    hashes = []
    for line in response.text.splitlines():
        parts = line.split(':')
        if len(parts) == 2: # Ensure we have both hash and count
            hashes.append(parts)

    for h, count in hashes:
        if h == rest:
            return f"This password has been leaked {count} times! Consider changing it."

    return "This password has NOT been found in leaks."

def check_password():
    password = entry.get() # Get the password from the entry field
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    
    strength = check_password_strength(password)
    hibp_result = check_hibp(password)
    
    strength_label.config(text=f"Password Strength: {strength}")
    hibp_label.config(text=hibp_result)

def main():
    # GUI Setup
    root = tk.Tk()
    root.title("Password Strength Checker")
    root.geometry("400x200")

    # Center the window
    root.update_idletasks()
    width = 400
    height = 200
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Create a frame for the input and buttons
    frame = tk.Frame(root)
    frame.pack(pady=20)

    # Create a label and entry for password input
    tk.Label(frame, text="Enter Password:").pack()
    global entry  # Make entry global so check_password() can access it
    entry = tk.Entry(frame, width=30)
    entry.pack()

    # Create a button to check the password
    check_button = tk.Button(frame, text="Check Password", command=check_password)
    check_button.pack(pady=10)

    # Create labels to display results
    global strength_label, hibp_label  # Make labels global so they can be updated
    strength_label = tk.Label(frame, text="Password Strength: ", fg="black")
    strength_label.pack()

    hibp_label = tk.Label(frame, text="", wraplength=350, fg="black")
    hibp_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
