import java.util.Arrays;

public class Counter
{
public static void countFreq(int arr[], int n)
{
    boolean visited[] = new boolean[n];

    Arrays.fill(visited, false);


    for (int i = 0; i < n; i++) {


        if (visited[i] == true)
            continue;


        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                visited[j] = true;
                count++;
            }
        }
        System.out.println(arr[i] + "         " + count);
    }
}


public static void main(String []args)
{
	System.out.println("Number    Count");
    int arr[] = new int[]{15,40,28,62,15,15,28,13,62,65,48,95,65,62,65,95,95 };
    int n = arr.length;
    countFreq(arr, n);
}
}