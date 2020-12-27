'''
1704. Determine if String Halves Are Alike
Problem Link : https://leetcode.com/problems/determine-if-string-halves-are-alike/
Runtime: 36 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def halvesAreAlike(self, s):
        s=s.lower()
        a,b=0,0
        for i in range(len(s)/2):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                a+=1
        for j in range(len(s)/2,len(s)):
            if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u':
                b+=1
        if a==b:
            return True
        else:
            return False