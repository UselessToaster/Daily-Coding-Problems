package Hard;
/* 
This problem was asked by Stripe.
Difficulty: Hard

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.*/
import java.util.Arrays;

class DCP_4 {
   public static void main(String [] args){
        //test data
        int [] data = {1, 2, 0};
        int missingNumber = missingInt(data);

        //display results
        System.out.println("The smallest missing positive integer is: " + missingNumber);
   } 
   public static int missingInt(int[] input){
        //sort given array
        Arrays.sort(input);

        //
        int count = 1;
        for(int elem: input ){
            if (elem > 0){              //bypass negative numbers
                if (count == elem){
                    count++;            //continues loop if consecutive number exists
                }
                else{
                    return count;       //ends loop if missing positive int is found
                }
            }
        }
        return count;                   //returns next consecutive number if all positive ints are accounted for
   }
}
