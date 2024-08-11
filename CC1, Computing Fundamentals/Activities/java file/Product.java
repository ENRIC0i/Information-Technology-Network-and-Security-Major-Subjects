/* Programmed by: Abenes, Enrico O.
   Program Title: Product.java
   Program Date: July 11, 2023*/

package intl.cc1;

public class Product {
    public static double printProduct(double x, double y) {
        double producto = x * y;
        return producto;
    }
    
    public static void main(String[] args) {
        double a = 4.6;
        double b = 5.9;
        
        double resulta = printProduct(a, b);
        System.out.println("Product = " + resulta);
    }
}
