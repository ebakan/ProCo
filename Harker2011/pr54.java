import java.util.Scanner;

public class pr54 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		byte[][] grid = new byte[10][10];
		Scanner scan = new Scanner(System.in);
		for(int i = 0; i < 10; i++){
			String newRow = scan.nextLine();
			byte[] newRowBytes = newRow.getBytes();
			for(int j = 0; j < 10; j++){
				grid[i][j] = newRowBytes[j];
			}
		}
		/*
		for(int i = 0; i < 10; i++){
			System.out.println(new String(grid[i]));
		}*/
		String[] words = new String[10];
		for(int i = 0; i < 10; i++)
			words[i] = scan.nextLine();
		boolean[] wordsFound = new boolean[10];
		for(int k = 0; k < words.length; k++){
			//First find the first letter of the word
			String word = words[k];
			for(int i = 0; i < 10; i++){
				for(int j = 0; j < 10; j++){
					if(grid[i][j] == word.getBytes()[0]){
						//Trying all vectors;
						for(int addRow = -1; addRow < 1; addRow++){
							for(int addCol = -1; addCol < 1; addCol++){
								if(addCol + addRow > 0)
									if(recurseSearch(word, grid, i, j, addRow, addCol))
										wordsFound[k] = true;
							}
						}
					}
				}
			}
		}
		for(boolean found: wordsFound){
			if(found)
				System.out.println("yes");
			else
				System.out.println("no");
		}
	}
	private static boolean recurseSearch(String word, byte[][] grid, int row, int col, int addRow, int addCol){
		//CHECK BOUNDS of grid
		if(row < 0 || row > 9 || col < 0 || col > 9)
			return false;
		if(grid[row][col] != word.getBytes()[0]){ //IF the first letter of the word is not equal to the grid coordinate we were passed, return false
			return false;
		}
		String newWord = word.substring(1);
		if(newWord.length() == 0)
			return true; //We have no more of the word to parse, therefore we are done.
		return recurseSearch(newWord, grid, row+addRow, col+addCol, addRow, addCol);
	}
}
