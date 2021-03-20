'''
3. Longest Substring Without Repeating Characters
Problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Runtime: 876 ms
Memory Usage: 14.5 MB
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans,m,le=0,0,len(set(s))
        while le>0:
            for i in range(len(s)):
                t=len(s[i:i+le])
                if t>m:
                    if t==len(set(s[i:i+le])):
                        if m<t:
                            m=t
            le-=1
        return m