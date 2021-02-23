'''
392. Is Subsequence
Problem Link : https://leetcode.com/problems/is-subsequence
Runtime: 12 ms
Memory Usage: 13.7 MB
'''
class Solution(object):
    def isSubsequence(self, s, t):    
        count=len(s)
        check=0
        if count<=len(t):
            for k in range(count):
                if s[k] in t:
                    t=''+t[t.index(s[k])+1:]
                    check+=1
        return count==check