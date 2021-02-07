'''
1753. Maximum Score From Removing Stones
Problem Link : https://leetcode.com/problems/maximum-score-from-removing-stones
Runtime: 32 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def maximumScore(self, a, b, c):
        return min((a+b+c)/2,a+b+c-max(a,b,c))