/*
1342. Number of Steps to Reduce a Number to Zero
**********
Problem Link : https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Submission detail : https://leetcode.com/submissions/detail/302688493/
Runtime: 0 ms, faster than 100.00% of Java online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 36.3 MB, less than 100.00% of Java online submissions for Number of Steps to Reduce a Number to Zero.
**********
*/
class Solution {
    public int numberOfSteps (int num) {
            int step=0;
            while(num!=0)
            {
                 if(num%2==0)
                {
                    num=num/2;
                }
                else
                {
                    num=num-1;
                }   
                step++;
            }
        return step;
    }
}
