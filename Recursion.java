import java.util.Scanner;

public class Recursion{
    /**
     * @param str string to be searched
	 * @param c character to be searched for
	 * @return # of instances of c in str
     */
    public static int count(String str, char c){
        if (str.length() == 0){
            return 0;
        }
        else if (str.charAt(0) == c){
            return 1 + count(str.substring(1), c);
        }
        else{
            return 0 + count(str.substring(1), c);
        }
    }

    /**
     * @param str the string that will be passed to helper method
     * calls a helper method to print all permutations of str
     */
    public static void permutations(String str){
        permutations("", str);
    }

    /**
     * @param s1 string that characters from s2 will be pushed into in subsequent calls
     * @param s2 characters will be pushed from this string to s1 in subsequent calls
     * helper method for permutations function, prints all permutations of the string passed to that function
     */
    public static void permutations(String s1, String s2){
        if (s2.length() == 0){
            System.out.println(s1);
        }
        else{
            for (int i = 0; i < s2.length(); i++){
                permutations(s1 + s2.charAt(i), s2.substring(0, i) + s2.substring(i + 1));
            }
        }
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string: ");
        String str = scanner.nextLine();
        System.out.println("Enter a character: ");
        char c = scanner.nextLine().charAt(0);
        int count = count(str, c);
        System.out.println(c + " appears " + count + " times in \"" + str + "\"");
        System.out.println("Enter a string: ");
        str = scanner.nextLine();
        permutations(str);
    }
}