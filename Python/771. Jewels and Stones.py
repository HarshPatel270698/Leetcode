'''
771. Jewels and Stones
Problem Link : https://leetcode.com/problems/jewels-and-stones/submissions/
Runtime: 16 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        j=list(jewels)
        s=list(stones)
        c=0
        for x in range(len(s)):
            for y in range(len(j)):
                if s[x]==j[y]:
                    c+=1
        return c