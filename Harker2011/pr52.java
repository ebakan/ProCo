import java.util.Scanner;
import java.util.Arrays;
public class pr52 {

	/**
	 * @param args
	 */
	boolean[] primes = new boolean[2500];
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String input = scan.nextLine();
		String[] nums = input.split(" ");
		int low = Integer.parseInt(nums[0]);
		int high = Integer.parseInt(nums[1]);
		pr52 temp = new pr52();
		temp.fillSieve();
		for(int i = low; i <= high; i++){
			if(temp.isPrime(i)){
				System.out.print("" + i + " ");
			}
		}
	}
	public void fillSieve(){
		Arrays.fill(primes, true);
		primes[0] = primes[1] = false;
		for (int i = 2; i < primes.length ; i++){
			if(primes[i]){
				for(int j=2;i*j<primes.length;j++){
					primes[i*j] = false;
				}
			}
		}
	}
	boolean isPrime(int n){
		return primes[n];
	}
}
