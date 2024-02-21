import java.util.*;


public class workArray
{
	public static void main(String[] args)
	{

		Scanner sc = new Scanner(System.in);
		Random rng = new Random();

		System.out.println("How big do you want the array to be?");
		int size = sc.nextInt();

		int[] arr = new int[size];


		for(int i = 0; i < arr.length; i++)
		{
			arr[i] = rng.nextInt(11)+20; // generates numbers between 20 and 30

			System.out.print(arr[i] + ", ");
		}

		int  highesValue = highest(arr); // dont need to put the square brackets because then it expects a location
		System.out.println("The highest value is " + highesValue);

		int total  = sum(arr);
		System.out.println("Your total is " + total);

		double Ave = average(arr);
		System.out.println("Your average is " + Ave);


		boost(arr);
		for(int i = 0; i < arr.length; i++)
		{
			System.out.print(arr[i] + ", ");
		}

	}

	public static int highest(int[] array)
	{
		int highest = array[0];
		for(int i = 1; i < array.length; i ++)
		{
			if(array[i] > highest)
			{
				highest = array[i];


			}

		}
		return highest;
	}
	public static int sum(int[] array)
	{
		int total = 0;

		for(int i = 0; i < array.length; i++)
		{
			total += array[i];


		}
		return total;
	}
	public static double average(int[] array)
	{
		double average = 0;
		int sum = sum(array);

		average = sum / (double)array.length;

		return average;

	}
	public static void boost(int[] array)
	{
		for(int i = 0; i < array.length; i++)
		{
			array[i] *= 10;
		}
		// no need to return only if we are dealing with higher demensions
	}
}