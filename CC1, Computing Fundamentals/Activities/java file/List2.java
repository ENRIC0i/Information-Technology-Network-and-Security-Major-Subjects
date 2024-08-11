/* Programmed by: Abenes, Enrico O.
   Program Title: List2.java
   Program Date: July 11, 2023*/

package intl.cc1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class List2 {
    public static void main(String[] args) {
        String search_input, input;
        boolean hanap = false;
        int search_value, ctr = 0;
        
        int[] list1 = new int[10];
        int[] list2 = new int[10];
        int[] list3 = new int[10];
        
        BufferedReader basa = new BufferedReader(new InputStreamReader(System.in));
        
        try {
            System.out.println("Enter Ten(10) Integer Values for List1");
            for (int i = 0; i < 10; i++) {
                System.out.print("Input value for list1[" + i + "] = ");
                input = basa.readLine();
                list1[i] = Integer.parseInt(input);
            }
            
            System.out.println(" ");
            System.out.println("Enter Ten(10) Integer Values for List2");
            for (int i = 0; i < 10; i++) {
                System.out.print("Input value for list2[" + i + "] = ");
                input = basa.readLine();
                list2[i] = Integer.parseInt(input);
            }
        
            System.out.println(" ");
            System.out.print("List1 : ");
            for (int i = 0; i < 10; i++) {
                System.out.print(list1[i] + "  ");
            }
            System.out.println();
        
            System.out.print("List2 : ");
            for (int i = 0; i < 10; i++) {
                System.out.print(list2[i] + "  ");
            }
            System.out.println();
        
            for (int i = 0; i < 10; i++) {
                list3[i] = list1[i] + list2[i];
            }
        
            System.out.print("List3 : ");
            for (int i = 0; i < 10; i++) {
                System.out.print(list3[i] + "  ");
            }
            System.out.println();

            System.out.println(" ");
            System.out.print("Input value to search in List3: ");
            search_input = basa.readLine();
            search_value = Integer.parseInt(search_input);
            
            StringBuilder lokasyon = new StringBuilder();
            
            System.out.println(" ");
            for (int i = 0; i < 10; i++) {
                if (list3[i] == search_value) {
                    if (!hanap) {
                        System.out.println("The value " + search_value + " is in List3!");
                        hanap = true;
                    }
                    ctr++;
                    lokasyon.append("list3[").append(i).append("]. ");
                }
            }
            
            if (hanap) {
                System.out.println("There are " + ctr + " of it in List 3.");
                System.out.println("Located at: " + lokasyon.substring(0, lokasyon.length() - 2));
            } else {
                System.out.println("The value " + search_value + " is not found in List3");
            }
            
        } catch (IOException e) {
            System.out.println("Error!");
        }
    }
}
