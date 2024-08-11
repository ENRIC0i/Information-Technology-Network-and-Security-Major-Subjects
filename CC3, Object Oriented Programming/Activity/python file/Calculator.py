# Programmed by: Abenes, Enrico O.
# Program Date: September 27, 2023
# Activity: Calculator

class my_calculator:

    def sum(self, numba1, numba2):
        return numba1 + numba2

    def difference(self, numba1, numba2):
        return numba1 - numba2

    def product(self, numba1, numba2):
        return numba1 * numba2

    def quotient(self, numba1, numba2):
        if numba2 == 0:
            return print("Cannot divided by zero")
        return numba1 / numba2

    def odd_number(self, numba3):
        return numba3 % 2 != 0

    def even_number(self, numba3):
        return numba3 % 2 == 0

    def positive_number(self, numba3):
        return numba3 > 0

    def negative_number(self, numba3):
        return numba3 < 0

def main_menu():
    calculator = my_calculator()

    while True:
        print("_________________________")
        print("        Main Menu        ")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Odd Integer Checker")
        print("6: Even Integer Checker")
        print("7: Positive Integer Checker")
        print("8: Negative Integer Checker")
        print("9: Exit")

        pili_kapo = int(input("Enter(1-9): "))

        if pili_kapo == 1:
            print("_________________________")
            print("        Addition         ")
            numba1 = int(input("Enter the first number: "))
            numba2 = int(input("Enter the second number: "))
            print(" ")
            print("Solution: ", numba1, " + ", numba2)
            sum_result = calculator.sum(numba1, numba2)
            print("Result: ", sum_result)
        elif pili_kapo == 2:
            print("_________________________")
            print("       Subtraction       ")
            numba1 = int(input("Enter the first number: "))
            numba2 = int(input("Enter the second number: "))
            print(" ")
            print("Solution: ", numba1, " - ", numba2)
            difference_result = calculator.difference(numba1, numba2)
            print("Result: ", difference_result)
        elif pili_kapo == 3:
            print("_________________________")
            print("      Multiplication     ")
            numba1 = int(input("Enter the first number: "))
            numba2 = int(input("Enter the second number: "))
            print(" ")
            print("Solution: ", numba1, " x ", numba2)
            product_result = calculator.product(numba1, numba2)
            print("Result: ", product_result)
        elif pili_kapo == 4:
            print("_________________________")
            print("         Division        ")
            numba1 = int(input("Enter the first number: "))
            numba2 = int(input("Enter the second number: "))
            print(" ")
            print("Solution: ", numba1, " / ", numba2)
            quotient_result = calculator.quotient(numba1, numba2)
            print("Result: ", quotient_result)
        elif pili_kapo == 5:
            print("_________________________")
            print("        Odd Checker      ")
            numba3 = int(input("Enter a number: "))
            odd_result = calculator.odd_number(numba3)
            if odd_result == True:
                print("The inputted number(", numba3, ") is an odd integer.")
            else:
                print("The inputted number(", numba3, ") is not an odd integer.")
        elif pili_kapo == 6:
            print("_________________________")
            print("       Even Checker      ")
            numba3 = int(input("Enter a number: "))
            even_result = calculator.even_number(numba3)
            if even_result == True:
                print("The inputted number(", numba3, ") is an even integer.")
            else:
                print("The inputted number(", numba3, ") is not an even integer.")
        elif pili_kapo == 7:
            print("_________________________")
            print("     Positive Checker    ")
            numba3 = int(input("Enter a number: "))
            positive_result = calculator.positive_number(numba3)
            if positive_result == True:
                print("The inputted number(", numba3, ") is a positive integer.")
            else:
                print("The inputted number(", numba3, ") is not a positive integer.")
        elif pili_kapo == 8:
            print("_________________________")
            print("    Negative Checker    ")
            numba3 = int(input("Enter a number: "))
            negative_result = calculator.negative_number(numba3)
            if negative_result == True:
                print("The inputted number(", numba3, ") is a negative integer.")
            else:
                print("The inputted number(", numba3, ") is not a negative integer.")
        elif pili_kapo == 9:
            print("Thank you for using our calculator")
            print("Terminating the program")
            break
        else:
            print("Invalid input")
            print("Please try again")

if __name__ == "__main__":
    main_menu()
