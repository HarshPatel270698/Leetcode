/*
1221. Split a String in Balanced Strings
**********
Problem Link : https://leetcode.com/problems/split-a-string-in-balanced-strings/
Submission : https://leetcode.com/submissions/detail/302698563/
Runtime: 1 ms, faster than 21.26% of Java online submissions for Split a String in Balanced Strings.
Memory Usage: 37.8 MB, less than 100.00% of Java online submissions for Split a String in Balanced Strings.
**********
*/
class Solution {
    public int balancedStringSplit(String s) {
        int r=0,l=0,count=0;
        String rs="R";
        for(int i=0;i<s.length();i++)
        {
                String temp=String.valueOf(s.charAt(i));
                if(temp.equals("R"))
                    {
                        r++;
                    }
                else
                   {
                       l++;
                   }
           if(r==l)
           {
               count++;
           }
        }
      return count;
    }
}
