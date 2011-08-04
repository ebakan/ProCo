import java.util.*;
public class adv92 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String[] firstLine = sc.nextLine().split(" ");
		int edges = Integer.parseInt(firstLine[1]);

		Route[] master = new Route[edges];

		for(int x = 0; x < edges; x++)
		{
			String[] locStr = sc.nextLine().split(" ");
			int first = Integer.parseInt(locStr[0]);
			int second = Integer.parseInt(locStr[1]);
			int val = Integer.parseInt(locStr[3]);

			master[0] = new Route(first, second, val);
		}

		int masterWeight = 0;

		for(int x = 0; x < edges; x++){
			int locY = master[x].getY();
			for(int y = 0; y < edges; y++){
				if(!(y==x)){
					int nextLocX = master[y].getX();
					int nextLocY = master[y].getY();
					
					//if()
				}
			}
		}

	}

}

class Route{
	int left, right, weight;

	public Route(int l, int r, int w){
		left = l;
		right = r;
		weight = w;
	}

	public int getX() { return left; }
	public int getY() { return right; }
	public int getWeight() { return weight; }
}
