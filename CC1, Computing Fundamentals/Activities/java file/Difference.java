/* Programmed by: Abenes, Enrico O.
   Program Title: Difference.java
   Program Date: July 11, 2023*/

package intl.cc1;

public class Difference {
    public static int printDifference(int x, int y) {
        int negatibo = x - y;
        return negatibo;
    }
    
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        
        int resulta = printDifference(a, b);
        System.out.println("Difference = " + resulta);
    }
}
