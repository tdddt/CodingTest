package java;

public class Factorial {

    // 반복
    public static int factorialIterative(int n){
        int result = 1;

        for (int i=1;i<=n;i++){
            result*=i;
        }
        return result;
    }

    // 재귀
    public static int factorialRecursive(int n){
        if(n<=1) return 1;
        return n*factorialRecursive(n-1);
    }
    public static void main(String[] args){
        factorialIterative(5);
        factorialRecursive(5);
    }
}
