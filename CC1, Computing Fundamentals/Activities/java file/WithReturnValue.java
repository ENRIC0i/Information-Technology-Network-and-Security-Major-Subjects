package intl.cc1;

public class WithReturnValue {
    public static int printSum(int x, int y) {
        z = x + y;
        return z;
    }
    
    public static void main(String[] args) {
        int a, b, c;
        
        System.out.println("Sum = " + printSum(5, 10));
        c = printSum(100, 300);
        System.out.println("c = " + c);
        
        a = 25;
        b = 75;
        
        System.out.println("Sum = " + printSum(a, b));
        System.out.println("Sum = " + Sum(a + 2, b - 3));
    }
}
