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
        //given input
        int [] numbers = {1, 2, 3, 4, 5};

        //Display solution using division
        int [] basic_result = basicSolution(numbers);
        System.out.println("basic solution with division:");
        for(int val : basic_result){
            System.out.print(val + " ");
        }
        System.out.println();

        ///Display solution without division
        int [] wOutDivResult = wOutDiv(numbers);
        System.out.println("solution without division:");
        for(int val : wOutDivResult){
            System.out.print(val + ", ");
        }
        System.out.println();
    }
    //method with division
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
    //method without division
    public static int[] wOutDiv(int[] inputArray){
        //establish output array
        int [] outputArray = new int [inputArray.length]; 
        //iterate through input array
        for(int i = 0; (i < inputArray.length); i++){
            int product = 1;
            int num = inputArray[i];
            //#get product of all values not equal to outer loop iterator
            for (int elem: inputArray){
                if (elem != num){
                    product *= elem;
                }
            }
            //add product to new array
            outputArray[i] = product;
        }
        return outputArray;
    }
}

