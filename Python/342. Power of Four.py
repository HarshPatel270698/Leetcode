'''
342. Power of Four
Problem Link : https://leetcode.com/problems/power-of-four/
Runtime: 16 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def isPowerOfFour(self, n):
        if n==0:
            return False
        if n==1:
            return True
        ans=1
        while ans<=abs(n):
            print n,ans
            ans*=4
            if ans==n:
                return True