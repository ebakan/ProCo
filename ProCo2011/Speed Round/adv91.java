import java.util.*;
public class adv91 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		boolean done = false;
		ArrayList<Domino> dominos = new ArrayList<Domino>();

		int n = Integer.parseInt(sc.nextLine());
		String topRowString = sc.nextLine();//.split(" ");
		String bottomRowString = sc.nextLine();//.split(" ");

		int[] topRow = new int[n];
		int[] bottomRow = new int[n];

		for(int x = 0; x < n; x++){
			topRow[x] = Integer.parseInt("" +topRowString.charAt(x));
			bottomRow[x] = Integer.parseInt("" + bottomRowString.charAt(x));
		}
		if(n == 1)
			if(topRow[0] == bottomRow[0])
			{
				System.out.println("REALITY");
				done = true;
			}
		
		if(!done)
		{
		for(int x = 0; x < n-1; x++){
			Domino locDom = new Domino(topRow[x], topRow[x+1]);
			
			for(Domino y : dominos)
				if(y.equals(locDom) && x >= n - 2){
					System.out.println("REALITY");
					done = true;
					break;
				}
			dominos.add(locDom);

		}
		}
		if(!done){
			for(int x = 0; x < n-1; x++){
				Domino locDom = new Domino(bottomRow[x], bottomRow[x+1]);
				for(Domino y : dominos)
					if(y.equals(locDom) && x >= n - 2){
						System.out.println("REALITY");
						done = true;
						break;
					} 
				dominos.add(locDom);
			}
		}

		if(!done) System.out.println("DREAM");



	}

}

class Domino
{
	int left, right;
	public Domino(int l, int r)
	{
		left = l;
		right = r;
	}

	public boolean equals(Domino d)
	{
		if(d.left == this.left && d.right == this.right)
			return true;
		if(d.left == this.right && d.right == this.left)
			return true;
		return false;
	}
	
	public boolean reversed(Domino d)
	{
		if(d.left == this.right && d.right == this.left)
			return true;
		return false;
	}
}