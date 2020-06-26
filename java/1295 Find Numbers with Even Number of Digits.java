/*
1295. Find Numbers with Even Number of Digits
**********
Problem Link : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Runtime: 0 ms
Memory Usage: 45.1 MB
**********
*/
class Solution {
    public int findNumbers(int[] nums) {
        int even=0;
        for(int i=0;i<nums.length;i++)
        {
            if((nums[i]>=10 && nums[i]<100)||(nums[i]>=1000 && nums[i]<10000))
            {
                even++;
            }
        }
        return even;
    }
}
