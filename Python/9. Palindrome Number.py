'''
9. Palindrome Number
Problem Link : https://leetcode.com/problems/palindrome-number/
Runtime: 24 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]