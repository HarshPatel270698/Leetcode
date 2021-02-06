'''
14. Longest Common Prefix
Problem Link : https://leetcode.com/problems/longest-common-prefix
Runtime: 12 ms
Memory Usage: 13.8 MB
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs==[] or "" in strs:
            return ""
        else:
            l=[]
            small=strs[0]
            for i in strs:
                if len(i)<len(small):
                    small=i
            for i in small:
                l.append(i)
            for i in strs:
                if len(l)>=len(i):
                    min=len(i)
                else:
                    min=len(l)
                for j in range(0,min):
                    if l[j]!=i[j]:
                        del l[j:]
                        break
            return "".join(l)