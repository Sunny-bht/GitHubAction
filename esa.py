import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak password. It should be at least 8 characters long."
    if not re.search(r"[a-z]", password):
        return "Weak password. It should contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return "Weak password. It should contain at least one uppercase letter."
    if not re.search(r"\d", password):
        return "Weak password. It should contain at least one number."
    return "Strong password!"

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_password_strength(password))


#Code zum Teil gefüllt von ChatGPT
