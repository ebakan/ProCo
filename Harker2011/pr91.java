import java.util.Scanner;

public class pr91 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int numKeyLines = Integer.parseInt(sc.nextLine());
		String[] keyLines=new String[numKeyLines];
		for(int i=0;i<numKeyLines;i++)
			keyLines[i]=sc.nextLine();
		String out="";
		int numOutChars=Integer.parseInt(sc.nextLine());
		for(int i=0;i<numOutChars;i++) {
			String[] nums = sc.nextLine().split(" ");
			int row=Integer.parseInt(nums[0]);
			int col=Integer.parseInt(nums[1]);
			out+=keyLines[row-1].charAt(col-1);
		}
		System.out.println(out);
	}

}
