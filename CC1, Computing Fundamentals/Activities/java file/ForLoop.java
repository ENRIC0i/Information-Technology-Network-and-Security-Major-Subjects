/* Programmed by: Abenes, Enrico O.
   Program Title: ForLoop.java
   Program Date: July 10, 2023*/

package intl.cc1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class ForLoop {
    public static void main(String[] args) {
        int start, end, step;
        String choice;

        BufferedReader basa = new BufferedReader(new InputStreamReader(System.in));

        for (choice = "Y"; choice.equals("Y"); ) {
            try  {
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
                for (int i = start; i <= end; i+= step) {
                    System.out.println(i);
                }

                System.out.println();
                System.out.print("Do you want to try again (Y/N)? ");
                choice = basa.readLine().toUpperCase();
            } catch (IOException | NumberFormatException e) {
                System.out.println("Error!");
                choice = "Y";
            }
        }
    }
}