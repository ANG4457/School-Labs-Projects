import java.util.Scanner;
public class Problem4USETHIS
{
public static void main(String[] args)
{
Scanner sc = new Scanner(System.in);
int number=0;
number=sc.nextInt();

while (number>0)
{
int digit=number%10;

System.out.print(" ");

System.out.print(digit);
number=number/10;
}
}
}