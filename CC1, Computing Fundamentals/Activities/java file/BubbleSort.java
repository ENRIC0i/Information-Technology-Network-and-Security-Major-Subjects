/* Programmed by: Abenes, Enrico O.
   Program Title: BubbleSort.java
   Program Date: July 11, 2023*/

package intl.cc1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class BubbleSort {
    public static void main(String args[]) {
        BufferedReader basa = new BufferedReader(new InputStreamReader(System.in));
        
        try {
            System.out.print("Enter the size of list: ");
            int laki = Integer.parseInt(basa.readLine());
            
            int[] list = new int[laki];
            
            System.out.println(" ");
            System.out.println("Enter the values for the list: ");
            for (int i = 0; i < laki; i++) {
                System.out.print("Value " + (i+1) + ": ");
                list[i] = Integer.parseInt(basa.readLine());
            }
            
            for (int i = 0; i < laki - 1; i++) {
                for (int j = 0; j < laki - i - 1; j++) {
                    if (list[j] > list[j + 1]) {
                        int temp = list[j];
                        list[j]= list[j + 1];
                        list[j + 1] = temp;
                    }
                }
            }
            
            System.out.println(" ");
            System.out.print("Sorted list: ");
            for (int i = 0; i < laki; i++) {
                System.out.print(list[i] + " ");
            }
        } catch (IOException e) {
            System.out.println("Error!");
        } catch (NumberFormatException e) {
            System.out.println("Invalid. Please input a number.");
        }
    }
}
