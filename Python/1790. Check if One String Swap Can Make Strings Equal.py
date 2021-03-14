'''
1790. Check if One String Swap Can Make Strings Equal
Problem Link : https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
Runtime: 20 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        n=0
        ans=0
        if s1==s2:
            return True
        if set(s1)==set(s2):
            while len(s1)!=n:
                if s1[n]!=s2[n]:
                    ans+=1
                n+=1
        return ans==2