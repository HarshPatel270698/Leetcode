'''
784. Letter Case Permutation
Problem Link : https://leetcode.com/problems/letter-case-permutation/
Runtime: 32 ms
Memory Usage: 14.1 MB
'''
class Solution(object):
    def letterCasePermutation(self, S):
        a = ['']
        for i in S:
            t = []
            for j in a:
                if i.isalpha():
                    t.append(j + i.upper())            
                    t.append(j + i.lower())
                else:
                    t.append(j + i)
            a = t
        return a