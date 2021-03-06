/*
771. Jewels and Stones
**********
Problem Link : https://leetcode.com/problems/jewels-and-stones/
Runtime: 1 ms
Memory Usage: 41.6 MB
**********
*/
class Solution {
    public int numJewelsInStones(String J, String S) {
    int jewelcount=0;
     for(int a=0;a<S.length();a++)
     {
         Character stone=S.charAt(a);
         int hashs=stone.hashCode();
         for(int b=0;b<J.length();b++)
         {
            Character jewel=J.charAt(b);
            int hashj=jewel.hashCode();
             if(hashs==hashj)
             {
                 jewelcount++;
             }
         }
     }
        return jewelcount;
    }
}
