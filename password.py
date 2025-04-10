# IMPORTS:
import string
import random

# INITIAL VARIABLES:
password = ""
password_lenght = 16
expresion = list(string.ascii_letters) + [str(i) for i in range(1, 10)] + list("!@#$%^&*()-_=+[]{};:,.<>?/")

# FUNCTIONS:
def main(password, password_lenght, expresion):
    print("PASSWORD GENERATOR:")
    for _ in range(password_lenght):
        password += random.choice(expresion)
        
        # IF NO NUMBERS PUT ONE AT THE END:
        if not any(c.isdigit() for c in password):
            random_number = random.choice([str(i) for i in range(1, 10)])
            password = password[:-1] + random_number

    return password

# INVOCATION:
new_password = main(password, password_lenght, expresion)
print(f"New Password: {new_password}")