'''
1323. Maximum 69 Number
Problem Link : https://leetcode.com/problems/maximum-69-number/
Runtime: 28 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def maximum69Number (self, num):
        n=str(num)
        k=n.replace('6', '9', 1)
        return k