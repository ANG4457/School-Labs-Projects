public class 2dArrays
{
	public static void main(String[] args)
	{
		int[] arr = {1, 2, 3, 4, 5};
		int search = 3;


		for(int i = 0; i < arr.length; i++)
		{
			if(search == arr[i])
			{
				System.out.println("The index is " + i); // shows actual location
			}
		}
	}
}