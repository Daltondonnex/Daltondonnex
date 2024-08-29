import java.util.Scanner;

public class ConsecutiveIntegerCheckingGCD {
    public static int gcd(int a, int b) {
        
        int min = Math.min(a, b);
    
        for (int i = min; i > 0; i--) {
            if (a % i == 0 && b % i == 0) {
                return i;
            }
        }
        return 1; // This line is never reached for positive a and b

        
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for input
        System.out.print("Enter the first number: ");
        int a = scanner.nextInt();
        System.out.print("Enter the second number: ");
        int b = scanner.nextInt();

        // Compute and display the GCD
        int result = gcd(a, b);
        System.out.println("GCD of " + a + " and " + b + " is: " + result);
        
        scanner.close();
    }
}
