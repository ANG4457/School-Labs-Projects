public class BreakIntegerExample3
{
public static void main(String[] args)
{
//an integer number to break
int number=1398754;
//while loop executes until the condition become false
while (number>0)
{
int digit=number%10;
//prints space between the digits
System.out.print(" ");
//prints the digits
System.out.print(digit);
//dividing the number by 10
number=number/10;
}
}
}