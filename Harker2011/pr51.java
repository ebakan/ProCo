import java.util.Scanner;

public class pr51 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count=0;
		String[] tmp = sc.nextLine().split(" ");
		int numRows = Integer.parseInt(tmp[0]);
		int numCols = Integer.parseInt(tmp[1]);
		int[][] nums = new int[numRows][numCols];
		
		int currPos = 0;
		
		while(count < numRows*numCols){
			String[] lines = sc.nextLine().split(" ");
			
			for(int i = Integer.parseInt(lines[1]); i > 0; i--)
			{
				int row = currPos / numCols;
				int col = currPos % numCols;
				nums[row][col] = Integer.parseInt(lines[0]);
				currPos++;
			}
			count += Integer.parseInt(lines[1]);
		}
		
		for(int r = 0; r < nums.length; r++){
			for(int c = 0; c < nums[r].length; c++){
				System.out.print(nums[r][c]);
			}
			System.out.println();
		}
		  

	}

}
