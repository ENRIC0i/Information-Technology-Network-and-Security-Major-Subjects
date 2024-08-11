/* Programmed by: Abenes, Enrico O.
   Program Title: WhileLoop.java
   Program Date: July 10, 2023*/

package intl.cc1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class WhileLoop {
    public static void main(String[] args) {
        int start, end, step;
        String choice;

        BufferedReader basa = new BufferedReader(new InputStreamReader(System.in));

        boolean tryAgain = true;
        while (tryAgain) {
            try {
                System.out.print("Input START value   = ");
                choice = basa.readLine();
                start = Integer.parseInt(choice);

                System.out.print("Input END value     = ");
                choice = basa.readLine();
                end = Integer.parseInt(choice);

                System.out.print("Input STEP value    = ");
                choice = basa.readLine();
                step = Integer.parseInt(choice);

                System.out.println();
                int i = start;
                while (i <= end) {
                    System.out.println(i);
                    i += step;
                }

                System.out.println();
                System.out.print("Do you want to try again (Y/N)? ");
                choice = basa.readLine().toUpperCase();
                tryAgain = choice.equals("Y");
            } catch (IOException | NumberFormatException e) {
                System.out.println("Error!");
                tryAgain = true;
            }
        }
    }
}
