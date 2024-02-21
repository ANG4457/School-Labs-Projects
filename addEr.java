public class addEr{
	static int adder(int[] arr){
		int sum = 0;
		for(int i =0; i<arr.length; i++){
			sum = sum + arr[i];
		}
		return sum;
	}
	static int adderRec(int[] arr, int index){
		int sum = 0;
		if(index >= 0){
			sum = arr[index] + adderRec(arr, index -1);
		}
		return sum;
	}

	public static void main(String []args){
		int[] arr = {1,2,3,4,5,6,7,8,90};
		System.out.println("for loop method" + adder(arr));

		System.out.println("rec method" + adderRec(arr, arr.length-1));

	}
}