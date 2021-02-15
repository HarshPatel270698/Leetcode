'''
205. Isomorphic Strings
Problem Link : https://leetcode.com/problems/isomorphic-strings/
Runtime: 112 ms
Memory Usage: 120 MB
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)==len(t) and len(set(s))==len(set(t)):
            dict={}
            temp=""
            for i in range(len(s)):
                dict[s[i]]=t[i]
            for i in range(len(s)):
                temp+=dict[s[i]]
            return temp==t