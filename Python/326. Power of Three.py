'''
326. Power of Three
Problem Link : https://leetcode.com/problems/power-of-three
Runtime: 52 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def isPowerOfThree(self, n):
        if n>=1:
            while n%3==0:
                n/=3
            return n==1
'''
Runtime: 72 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def isPowerOfThree(self, n):
        if n>=1:
            if n==1:
                return True
            ans=1
            while ans<=n:
                ans*=3
                if ans==n:
                    return True
