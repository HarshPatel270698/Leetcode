/*
1323. Maximum 69 Number
**********
Problem Link : https://leetcode.com/problems/maximum-69-number/
Submission : https://leetcode.com/submissions/detail/302708989/
Runtime: 0 ms, faster than 100.00% of Java online submissions for Maximum 69 Number.
Memory Usage: 36.3 MB, less than 100.00% of Java online submissions for Maximum 69 Number.
**********
*/
class Solution {
    public int maximum69Number (int num) {
        int rev=0,rev1=0,count=0;
        while(num>0)
      {
            int n=num%10;
            rev=rev*10+n;
            num=num/10;
      }
      while(rev>0)
      {
            int k=rev%10;
            if(count==0&&k==6)
            {
                k=9;
                count++;
            }
            rev1=rev1*10+k;
            rev=rev/10;
      }
        return rev1;     
    }
}
