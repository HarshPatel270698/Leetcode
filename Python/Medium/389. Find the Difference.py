'''
389. Find the Difference
Problem Link : https://leetcode.com/problems/find-the-difference/
Runtime: 24 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def findTheDifference(self, s, t):
        s=sorted(s)
        t=sorted(t)
        i,l=0,len(s)-1
        while i<=l:
            if s[i]!=t[i]:
                return t[i]
            i+=1
        return t[-1]