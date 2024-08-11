/* Programmed by: Abenes, Enrico O.
   Program Title: Accum2.java
   Program Date: July 10, 2023*/

package intl.cc1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Accum2 {
    public static void main(String[] args) {
        int i, n, sum_even = 0, sum_odd = 0;
        String input = " ";      
        
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        
        for (i = 0; i < 10; i++) {
            System.out.print("Input integer number: ");
            try {
                input = in.readLine();
            } catch (IOException e) {
                System.out.println("Error!");
            }
            
            n = Integer.parseInt(input);
            
            if (n % 2 == 0) {
                sum_even += n;
            } else {
                sum_odd += n;
            }
        }
        System.out.println("The sum of even integers is: " + sum_even);
        System.out.println("The sum of odd integers is: " + sum_odd);
    }
}
