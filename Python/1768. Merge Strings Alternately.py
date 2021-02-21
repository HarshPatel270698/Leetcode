'''
1768. Merge Strings Alternately
Problem Link : 
Runtime: 24 ms
Memory Usage: 13.8 MB
'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans=""
        w1=len(word1)
        w2=len(word2)
        if w1>=w2:
            l=w1
        else:
            l=w2
        for i in range(l):
            if i+1>w1:
                ans+=word2[i]
            elif i+1>w2:
                ans+=word1[i]
            else:
                ans+=word1[i]
                ans+=word2[i]
        return ans