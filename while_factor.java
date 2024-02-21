// I expanded on the loop and process we used in class//


import java.util.Scanner;

public class while_factor{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		// Scanner asks for inputs to multiply//

		long p = 0;
		long q = 0;
		System.out.println("What is your P value?");
		p = sc.nextLong();
		System.out.println("What is your Q Value?");
		q = sc.nextLong();

		// gathers the start and end time for the Mult//

		long startA =
		System.currentTimeMillis();
		long x = (p * q);

		long endA =
		System.currentTimeMillis();

		long ExeA = endA - startA;

	System.out.println("Your number is: " + x);
	System.out.println("The execution for the Mult. was: " + ExeA + " milliseconds");
	System.out.println("The factors of " + x + " are: ");


	long startb =
	System.currentTimeMillis();


		long n = x;
 		for (long i = 1; i <= x; i++) {
            if (n % i == 0) {
                System.out.println(i);
            }
		}

		long endB =
		System.currentTimeMillis();

		long ExeB = endB - endA;

		System.out.println("The time it took to execute factoring was: " + ExeB + " milliseconds");
		long sec = (ExeB / 1000);
		long minute = (sec / 60);

		System.out.println("the amount of seconds it took to factor was: " + sec + " seconds");
		System.out.println("the amount of minutes it took to factor was: " + minute + " minutes");
	}
}