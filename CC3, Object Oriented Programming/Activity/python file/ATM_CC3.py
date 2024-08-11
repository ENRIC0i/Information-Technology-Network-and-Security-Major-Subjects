# Programmed by: Abenes, Enrico O.
# Program Date: September 11, 2023

balance = 10000

def main_menu():
    while True:
        print("________________________")
        print("          Menu          ")
        print("1 - Check Balance")
        print("2 - Withdrawal")
        print("3 - Exit")
        print(" ")
        choice = input("Enter(1-3): ")
        print(" ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            print("____________________________")
            print("Thank you for using this ATM")
            print("        Logging out         ")
            exit()
        else:
            print("  Invalid Input  ")
            print("Please Try Again")

def check_balance():
    print("________________________")
    print("    Checking Balance    ")
    print(f"Your current balance: PHP {balance: .2f}")
    print(" ")

def withdraw():
    global balance
    print("________________________")
    print("       Withdrawal       ")

    while True:
        amount_str = input("Enter withdrawal amount: PHP ")

        if not amount_str.isdigit():
            print("Invalid input. Please enter numerical value")
            continue

        amount = float(amount_str)

        if amount <= 0:
            print("Invalid Amount")
            print("Please enter positive value")
            print(" ")
        elif amount > balance:
            print("Insufficient Balance")
            print("  Please Try Again  ")
            print(" ")
        else:
            balance -= amount
            print(f"Withdrawn amount: PHP {amount: .2f}")
            print("Denominations:")

            denominations = [1000, 100, 20, 1]

            for denom in denominations:
                if amount >= denom:
                    count = int(amount / denom)
                    amount -= count * denom
                    print(f"₱{denom} x {count} = ₱{count * denom}")

            balance -= amount
            break

main_menu()