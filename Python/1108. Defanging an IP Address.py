'''
1108. Defanging an IP Address
Problem Link : https://leetcode.com/problems/defanging-an-ip-address/
Runtime: 12 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.','[.]')