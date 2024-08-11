/* Programmed by: Abenes, Enrico O.
   Program Title: List.java
   Program Date: July 11, 2023*/

package intl.cc1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class List {
    public static void main(String[] args) {
        int list[] = new int[10];
        int i, num = 0;
        String input = " ";
        
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        
        for (i = 0; i < 10; i++) {
            list[i] = 0;
        }
        for (i = 0; i < 10; i++) {
            System.out.print("Input value for list [" + i + ") = ");
            try {
                input = in.readLine();
            } catch (IOException e) {}
                num = Integer.parseInt(input);
                list[i] = num;
            }
            
            for (i = 0; i < 10; i++) {
                System.out.println("list [" + i + "] = " + list[i]);
            }
    }
}