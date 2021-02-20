'''
1249. Minimum Remove to Make Valid Parentheses
Problem Link : https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Runtime: 92 ms
Memory Usage: 19.3 MB
'''
class Solution(object):
    def minRemoveToMakeValid(self, s):
        str=list(s)
        l=[]
        for i in range(len(s)):
            if str[i]=="(":
                l.append(i)
            elif str[i]==")":
                if l:
                    l.pop()
                else:
                    str[i]=""
        while l:
            str[l.pop()]=""
        return "".join(str)