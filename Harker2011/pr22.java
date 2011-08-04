import java.util.Scanner;

public class pr22 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double average=0;
		int n=sc.nextInt();
		for(int i=0;i<n;i++) {
			average+=sc.nextDouble();
		}
		average=(int)(average/n);
		char out;
		if(average>=93)
			out='A';
		else if(average>=83)
			out='B';
		else if(average>=73)
			out='C';
		else if(average>=60)
			out='D';
		else
			out='F';
		System.out.println(out);
			

	}

}
