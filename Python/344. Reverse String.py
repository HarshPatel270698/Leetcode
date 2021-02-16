'''
344. Reverse String
Problem Link : https://leetcode.com/problems/reverse-string/
Runtime: 176 ms
Memory Usage: 21.2 MB
'''
class Solution(object):
    def reverseString(self, s):
        s.append("")
        for i in range(1,(len(s)/2)+1):
            s[-1]=s[i-1]
            s[i-1]=s[-i-1]
            s[-i-1]=s[-1]
        s.pop(-1)