# Programmed by: Abenes, Enrico O.
# Program Title: Laboratory Activity - Password Checker
# Program Date: July 15, 2023

def check_password_strength(password):
    errors = []

    # Verify that the length of the password is no more than 8 characters.
    if len(password) < 8:
        errors.append("Password should have a minimum length of 8 characters.")

    # Verify the password to make sure it has at least one uppercase letter.
    if not any(char.isupper() for char in password):
        errors.append("Password should contain at least one uppercase letter.")

    # Verify the password to make sure it has at least one lowercase letter.
    if not any(char.islower() for char in password):
        errors.append("Password should contain at least one lowercase letter.")

    # Verify the password to make sure it has at least one digit.
    if not any(char.isdigit() for char in password):
        errors.append("Password should contain at least one digit.")

    # Verify the password to make sure it has at least one special character.
    if not any(not char.isalnum() for char in password):
        errors.append("Password should contain at least one special character.")

    return errors

# Start of loop.
while True:
    # Asking the user to enter a password (input)
    password = input("Enter your password: ")
    # Check the password's strength and obtain a list of mistakes
    errors = check_password_strength(password)

    # If no mistakes are identified, it will execute the assigned task.
    if len(errors) == 0:
        print("Password is strong. Good job!")
        # End of Loop: It will terminate the program if the conditions are met.
        break

    print("Password is weak.")
    print("The following conditions are not met:")
    # Print the list of conditions that a password entry doesn't meet.
    for error in errors:
        print(error)