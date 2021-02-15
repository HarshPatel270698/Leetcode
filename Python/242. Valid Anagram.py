'''
242. Valid Anagram
Problem Link : https://leetcode.com/problems/valid-anagram
Runtime: 28 ms
Memory Usage: 14.2 MB
'''
class Solution(object):
    def isAnagram(self, s, t):
        if set(s)==set(t) and len(s)==len(t):
            for i in set(s):
                if s.count(i)!=t.count(i):
                    return False
            return True
'''
Runtime: 552 ms
Memory Usage: 14.9 MB
'''           
class Solution(object):
    def isAnagram(self, s, t):
        sorts=""
        sortt=""
        for i in sorted(s):
            sorts+=i
        for i in sorted(t):
            sortt+=i
        return sorts==sortt