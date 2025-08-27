/*This problem was asked by Uber.
Difficulty: Hard

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the 
expected output would be [2, 3, 6].

Follow-up: what if you can't use division?*/
package Hard;
class DCP_2 {
    public static void main(String [] args){
        int [] numbers = {1, 2, 3, 4, 5};

        int [] basic_result = basicSolution(numbers);
        System.out.println("basic solution with division:\n");
        for(int val : basic_result){
            System.out.print(val + " ");
        }
        System.out.println();

        //Will finish with w/out division and improvement revisions in the morning 

        /*int [] basic_result = basicSolution(numbers);
        System.out.println("basic solution with division:\n");
        for(int val : basic_result){
            System.out.print(val + ", ");
        }
        System.out.println();
        */
    }
    public static int [] basicSolution(int[] inputArray){
        //get total product
        int product = 1;
        for(int num : inputArray){
            product *= num;
        }

        //divide given value to get solution
        int result;
        int [] outputArray = new int[inputArray.length];
        for(int i = 0; (i < inputArray.length); i++){
            result = product/inputArray[i];
            outputArray[i] = result;
        }

        return outputArray;
    }
}
