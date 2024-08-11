/* Programmed by:   Abenes, Enrico O.
                    Autor, Flix Nino
   Program Title:   TwoDimensionArrayActivity.java
   Program Date:    July 17, 2023 */

package intl.cc1;

import java.util.Scanner;

public class TwoDimensionArrayActivity2 {
    public static void main(String[] args) {
        int k, n, pili, halaga, hilera = 5, hanay = 5;
        
        int[][] matriks = new int[hanay][hilera];
        
        Scanner iskan = new Scanner(System.in);
        
        while (true) {
            System.out.println("_______________________");
            System.out.println("       Main Menu       ");
            System.out.println("1: Store a value");
            System.out.println("2: Retrieve a value");
            System.out.println("3: Exit");
            System.out.println();
            System.out.print("Enter you choice (1-3): ");
            pili = iskan.nextInt();
            iskan.nextLine();
            System.out.println("_______________________");
            
            switch (pili) {
                case 1:
                    System.out.print("Enter the value: ");
                    halaga = iskan.nextInt();
                    iskan.nextLine();
                
                    for (k = 0; k < matriks.length; k++) {
                        for (n = 0; n < matriks[k].length; n++) {
                            matriks[k][n] = halaga;
                        }
                    }
                    break;
                
                case 2:
                    System.out.print("Enter the row index(1-5): ");
                    hilera = iskan.nextInt();
                    iskan.nextLine();
                
                    System.out.print("Enter the column index(1-5): ");
                    hanay = iskan.nextInt();
                    iskan.nextLine();
                
                    System.out.println("The value at (" + hilera + ", " + hanay + ") is " + matriks[hilera][hanay]);
                    break;
                
                case 3:
                    System.out.println("Exiting the program...");
                    iskan.close();
                    System.exit(0);
                    break;
                
                default:
                    System.out.println("Invalid choice");
            }
            
            System.out.println("Array: ");
            for (k = 0; k < matriks.length; k++) {
                for (n = 0; n < matriks[k].length; n++) {
                    System.out.print(matriks[k][n] + "  ");
                }
                System.out.println();
            }
        }
    }
}