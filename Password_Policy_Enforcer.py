import re

def check_password_strength(password: str) -> bool:
    """
    Check if the password meets the following rules:
    - Minimum length of 12 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """

    # Rule 1: Minimum length
    if len(password) < 12:
        print("❌ Password must be at least 12 characters long.")
        return False

    # Rule 2: Uppercase letter
    if not re.search(r"[A-Z]", password):
        print("❌ Password must contain at least one uppercase letter.")
        return False

    # Rule 3: Lowercase letter
    if not re.search(r"[a-z]", password):
        print("❌ Password must contain at least one lowercase letter.")
        return False

    # Rule 4: Digit
    if not re.search(r"[0-9]", password):
        print("❌ Password must contain at least one digit.")
        return False

    # Rule 5: Special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("❌ Password must contain at least one special character.")
        return False

    print("✅ Password is strong and meets all requirements.")
    return True


# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)