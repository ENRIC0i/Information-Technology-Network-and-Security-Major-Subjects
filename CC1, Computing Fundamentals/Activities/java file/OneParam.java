package intl.cc1;

public class OneParam {
    public static void oneParam(int x) {
        System.out.println("Number is " + x);
    }
    
    public static void main(String[] args) {
        int x;
        x = 100;
        oneParam(x);
    }
}
