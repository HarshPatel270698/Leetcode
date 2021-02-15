'''
263. Ugly Number
Problem Link : https://leetcode.com/problems/ugly-numbe
Runtime: 12 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def isUgly(self, num):
        if num>=1:
            while num>=1:
                if num%5==0:
                    num/=5
                elif num%3==0:
                    num/=3
                elif num%2==0:
                    num/=2
                elif num==1:
                    return True
                else:
                    return False