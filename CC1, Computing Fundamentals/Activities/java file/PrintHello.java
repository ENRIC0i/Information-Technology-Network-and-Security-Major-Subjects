/* Programmed by: Abenes, Enrico O.
   Program Title: PrintHello.java
   Program Date: July 11, 2023 */

package intl.cc1;

public class PrintHello {
    public static void printHello() {
        System.out.print("Hello");
    }
    public static void printSpace() {
        System.out.print(" ");
    }
    public static void printWorld() {
        System.out.print("WORLD!");
    }
    public static void allTogetherNow() {
        printHello();
        printSpace();
        printWorld();
    }
    
    public static void main(String[] args) {
        allTogetherNow();
    }
}
