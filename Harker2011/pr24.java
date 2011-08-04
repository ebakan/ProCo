import java.util.Scanner;

public class pr24 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int len=Integer.parseInt(sc.nextLine());
		String[] binary = new String[len];
		String data=sc.nextLine();
		int currPos=0;
		System.out.println("ASDF: "+data.length());
		for(int i=0;i<data.length();i++) {
			binary[currPos]+=data.charAt(i);
			System.out.println("LEN" + binary[currPos].length());
			if(binary[currPos].length()>=8) {
				currPos++;
			}
		}
		int[] ints = new int[len];
		for(int i=0;i<len;i++) {
			System.out.println("WORKING: "+binary[i]);
			ints[i]=Integer.parseInt(binary[i], 2);
		}
		char[] chars = new char[len];
		for(int i=0;i<len;i++)
			chars[i]=(char)ints[i];
		for(int i=0;i<len;i++)
			System.out.print(chars[i]);
		System.out.flush();
	}

}
