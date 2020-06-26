/*
1108. Defanging an IP Address
**********
Problem Link : https://leetcode.com/problems/defanging-an-ip-address/
Runtime: 0 ms
Memory Usage: 40.5 MB
**********
*/
class Solution {
    public String defangIPaddr(String address) {
        String adr=address.replace(".","[.]");
        return adr; 
    }
}
