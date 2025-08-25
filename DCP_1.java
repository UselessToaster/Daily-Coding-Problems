/* Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?*/

//Disclaimer: This solution was derived with AI and is for my own learning purposes.
package Easy;
class DCP_1{
    public static void main(String[] args) {

        //establish input variables
        int[] nums = {10, 15, 3, 7};
        int k = 17;

        //call method and print output
        boolean result = twoSum(nums, k);
        System.out.println(result);
    }

    public static boolean twoSum(int[] nums, int k){
        for (int i = 0; i < nums.length; i++){
            for (int j = i; j < nums.length; j++){
                //can include everything in condition
                if (nums[i] + nums[j] == k){
                    return true; //ends the loop bc the method is exited this way
                }
            }
        }
        return false;
    }
}

/*Thoughts:
 * This solution is essentially what i came up with in python.
 * The AI originally imported some libraries but as i am refreshing myself i wanted to try it with base java.
 * Hopefully next time I can come up with a solution without consulting AI first.
 */

