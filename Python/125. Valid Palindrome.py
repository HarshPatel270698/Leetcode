'''
125. Valid Palindrome
Problem Link : https://leetcode.com/problems/valid-palindrome/
Runtime: 360 ms
Memory Usage: 14.6 MB
'''
class Solution(object):
    def isPalindrome(self, s):
        a=""
        for i in s:
            if i.isalpha() or i.isnumeric():
                a+=i.lower()
        return a==a[::-1]