import java.util.Scanner;
	public class EvenOdd
	{
		public static void main(String[] args)
		{
			Scanner input = new Scanner(System.in);

			int number = 0;
			System.out.println("Enter a number");
			number = input.nextInt();

			if(number%2 == 0)
			{
				System.out.println("your number is even");
			}
			else
			{
				System.out.println("Your nuber is odd");
			}
	    }
	}