public class GCD{
	//data members
	public static double start, end;
	public static double time1, time2, time3, time4;
	public static int iter1, iter2, iter3, iter4;
	
	/**
     * @param m first number
	 * @param n second number
	 * finds the greatest common denominator of m and n starting from 1 up 
     */
	//Time(n) = O(n)
	public static int gcd_1(int m, int n){
		iter1 = 0;
		int divisor = 1;
		for(int i=2; i<m && i<n; i++){
			iter1++;
			if(m%i == 0 && n%i == 0)
				divisor = i;
		}
		return divisor;
	} 
	/**
     * @param m first number
	 * @param n second number
	 * finds the greatest common denominator of m and n starting from n down
     */
	// Time(n) = O(n)
	public static int gcd_2(int m, int n){
		iter2 = 0;
		int divisor = 1;
		for(int i = n; i >= 1; i--){
			iter2++;
			if(m % i == 0 && n % i == 0){
			divisor = i; 
			break;
			}
		}
		return divisor;
	}
	/**
     * @param m first number
	 * @param n second number
	 * finds the greatest common denominator of m and n less than or equal to n/2
     */
	// Time(n) = O(n)
	public static int gcd_3(int m, int n) {
		iter3 = 0;
  		int divisor = 1;
  		if(m%n == 0) 
    		return n;
  		for(int i = n/2; i >= 1; i--){
			iter3++;
     		if(m%i == 0 && n%i == 0){
        		divisor=i; 
        		break;
			}
		}
		return divisor;
	}
	/**
     * @param m first number
	 * @param n second number
	 * finds the greatest common denominator of m and n using recursion
     */
	//Time(n) = O(log n)
	public static int gcd_4(int m, int n){
		iter4++;
   		if(m%n == 0) 
    		return n;
   		else
    		return gcd_4(n, m%n);
	}
	/**
     * Method to compare the number of iterations performed by gcd1, 2, 3, 4, for 20 different pairs of numbers
	 * Prints the paramters passed to each method and the numbers of iterations for each method
     */
	public static void compareIterations(){
		System.out.println("Comparing the gcd methods using the number of iterations");
		System.out.print(String.format("%-10s\t%-10s\t%-10s%-10s\t%-10s\t%-10s\n", "Number 1", "Number 2", "gcd_1", "gcd_2", "gcd_3", "gcd_4"));
		for (int i = 0; i < 20; i++){
            int n = (int)(Math.random() * 1000000);
            int m = (int)(Math.random() * 1000000);
                //ensure m >= n 
            if (m < n){
                int temp = n;
                n = m;
                m = temp;
            }
            GCD.gcd_1(m, n);
            GCD.gcd_2(m, n);
            GCD.gcd_3(m, n);
			iter4 = 0;
            GCD.gcd_4(m, n);
			System.out.print(String.format("%-10d\t%-10d\t%-10d%-10d\t%-10d\t%-10d\n", m, n, iter1, iter2, iter3, iter4));
		}
	}
	/**
     * Method to compare the execution time for gcd1, 2, 3, 4, for 20 different pairs of numbers
	 * Prints the parameters passed to each method and the execution times for each method
     */
	public static void compareTimes(){
		System.out.println("Comparing the gcd methods using the execution time");
		System.out.print(String.format("%-10s\t%-10s\t%-12s%-12s\t%-10s\t%-10s\n", "Number 1", "Number 2", "gcd_1", "gcd_2", "gcd_3", "gcd_4"));
		for (int i = 0; i < 20; i++){
            int n = (int)(Math.random() * 1000000);
            int m = (int)(Math.random() * 1000000);
                //ensure m >= n 
            if (m < n){
                int temp = n;
                n = m;
                m = temp;
            }
			start = System.nanoTime();
            GCD.gcd_1(m, n);
			end = System.nanoTime();
			time1 = end - start;
			start = System.nanoTime();
            GCD.gcd_2(m, n);
			end = System.nanoTime();
			time2 = end - start;
			start = System.nanoTime();
            GCD.gcd_3(m, n);
			end = System.nanoTime();
			time3 = end - start;
			iter4 = 0;
			start = System.nanoTime();
            GCD.gcd_4(m, n);
			end = System.nanoTime();
			time4 = end - start; 
			System.out.print(String.format("%-10d\t%-10d\t%-12.2f%-12.2f\t%-10.2f\t%-10.2f\n", m, n, time1, time2, time3, time4));
		}
	}

	public static void main(String[] args){
		compareIterations();
		System.out.println("");
		compareTimes();
	}
	/**The gcd methods with O(n) time complexity operate at mostly the same speed and with the same
	 * number of iterations. gcd_3 has around half the iterations and takes about half the time, but 
	 * also halves the number of possible values. gcd_4, however, which has time complexity O(log n), 
	 * runs much faster and uses less iterations. For example, when number 1 equals 992415 and number 2
	 * equals 549314, gcd_1 has 549312 iterations, while gcd_4 only has 17. gcd_4 is clearly much more
	 * efficient. This shows that functions with time complexity O(log n) will generally be much better 
	 * functions with time complexity O(n) or slower.
	**/
}
	






