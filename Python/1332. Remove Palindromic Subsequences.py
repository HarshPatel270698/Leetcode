'''
1332. Remove Palindromic Subsequences
Problem Link : https://leetcode.com/problems/remove-palindromic-subsequences/
Runtime: 8 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def removePalindromeSub(self, s):
        if len(s)==0:
            return 0
        if s==s[::-1]:
            return 1
        return 2