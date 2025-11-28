import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch.isalpha() for ch in password):
        score += 1
    if any(ch in string.punctuation for ch in password):
        score += 1

    return score

pwd = input("Enter a password to test: ")
strength = check_password(pwd)

levels = {
    1: "Weak",
    2: "Moderate",
    3: "Strong",
    4: "Very Strong"
}

print("Password Strength:", levels.get(strength, "Very Weak"))
