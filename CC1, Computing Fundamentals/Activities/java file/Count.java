/* Programmed by: Abenes, Enrico O.
   Program Title: Accum.java
   Program Date: July 10, 2023*/

package intl.cc1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Count {
    public static void main(String[] args) {
        int i, n, ctr;
        String input = " ";
        ctr = 0;
        
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        
        for (i = 1; i<= 10; i++) {
            System.out.print("Input integer number: ");
            try {
                input = in.readLine();
            } catch (IOException e) {
                System.out.println("Error!");
            }
            
            n = Integer.parseInt(input);
            
            if (n >= 0) {
                ctr = ctr + 1;
            }
        }
        System.out.println("The total value for counter is " + ctr);
    }
}
