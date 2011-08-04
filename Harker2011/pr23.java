import java.util.Scanner;

public class pr23 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int posR=0;
		int negR=0;
		do {
			String input=sc.nextLine();
			if(input.equals("*") || input.equals("**"))
				negR++;
			else
				posR++;
		}
		while(sc.hasNextLine());
		System.out.println(posR + " " + negR);
	}

}
