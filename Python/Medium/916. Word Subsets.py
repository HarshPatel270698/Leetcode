'''
916. Word Subsets
Problem Link : https://leetcode.com/problems/word-subsets
Runtime: 436 ms, faster than 100.00% of Python online submissions for Word Subsets.
Memory Usage: 19.2 MB, less than 7.14% of Python online submissions for Word Subsets.
'''
class Solution(object):
    def wordSubsets(self, A, B):
        s=set(A)
        d={}
        for i in B:
            for j in i:
                c=i.count(j)
                if j not in d or c>d[j]:
                    d[j]=i.count(j)
        for i in A:
            for j in d:
                c=i.count(j)
                if c<d[j]:
                    s.remove(i)
                    break
        return s
            