'''
1528. Shuffle String
Problem Link : https://leetcode.com/problems/shuffle-string/
Runtime: 44 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def restoreString(self, s, indices):
        d={}
        a=''
        for i in range(len(s)):
            d[indices[i]]=s[i]
        for i in d:
            a+=d[i]
        return a