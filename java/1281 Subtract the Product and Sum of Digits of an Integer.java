/*
1281. Subtract the Product and Sum of Digits of an Integer
**********
Problem Link : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Runtime: 0 ms
Memory Usage: 38.7 MB
**********
*/
class Solution {
    public int subtractProductAndSum(int n) {
            int rem=0;
	        int multi=1,sum=0;
              while(n>0)
              {
                  rem=n%10;
                  multi=rem*multi;
                  sum=rem+sum;
                  n=n/10;
              }
        return multi-sum;
    }
}
