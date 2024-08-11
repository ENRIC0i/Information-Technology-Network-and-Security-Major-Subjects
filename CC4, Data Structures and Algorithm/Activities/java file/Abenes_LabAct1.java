package intl.cc4;

import java.util.Scanner;

public class Abenes_LabAct1 {
    static double balance = 10000;
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("________________________");
            System.out.println("          Menu          ");
            System.out.println("1 - Check Balance");
            System.out.println("2 - Withdrawal");
            System.out.println("3 - Exit");
            System.out.println(" ");
            System.out.print("Enter(1-3): ");
            int choice = scanner.nextInt();
            System.out.println(" ");

            if (choice == 1) {
                balance();
            } else if (choice == 2) {
                withdraw(scanner);
            } else if (choice == 3) {
                System.out.println("____________________________");
                System.out.println("Thank you for using our ATM!");
                System.exit(0);
            } else {
                System.out.println("Incorrect input. Please try again.");
            }
        }
    }

    public static void balance() {
        System.out.println("________________________");
        System.out.println("    Checking Balance    ");
        System.out.printf("Your current balance is ₱ %.2f%n", balance);
        System.out.println(" ");
    }

    public static void withdraw(Scanner scanner) {
        System.out.println("________________________");
        System.out.println("       Withdrawal       ");

        while (true) {
            System.out.print("Type in the amount you want to withdraw: ₱");
            String amountStr = scanner.next();

            if (!amountStr.matches("\\d+")) {
                System.out.println("Invalid input. Please enter a numerical value");
                System.out.println(" ");
                continue;
            }

            double amount = Double.parseDouble(amountStr);

            if (amount <= 0) {
                System.out.println("Invalid amount. Please enter a positive value");
                System.out.println(" ");
            } else if (amount > balance) {
                System.out.println("The amount is greater than your current balance. Try again.");
                System.out.println(" ");
            } else {
                balance -= amount;
                System.out.printf("You have withdrawn ₱ %.2f%n", amount);
                System.out.println("Here is the denomination of the bills:");

            int[] denominations = {1000, 100, 20, 1};
            
            int[] denominationCount = new int[denominations.length];
            
            for (int i = 0; i < denominations.length; i++) {
                int denom = denominations[i];
                if (amount >= denom) {
                    int count = (int) (amount / denom);
                    amount -= count * denom;
                    denominationCount[i] = count;
                }
            }
            
            if (denominationCount[0] > 0) {
                System.out.printf("P1000: %d%n", denominationCount[0]);
            }
            if (denominationCount[1] > 0) {
                System.out.printf("P100: %d%n", denominationCount[1]);
            }
            if (denominationCount[2] > 0) {
                System.out.printf("P20: %d%n", denominationCount[2]);
            }
            
            int coinCount = denominationCount[3] + (int)(amount / 1);
            if (coinCount > 0) {
                System.out.printf("Coins: %d%n", coinCount);
            }
            
            balance -= amount;
            break;
            }
        }
    }
}
