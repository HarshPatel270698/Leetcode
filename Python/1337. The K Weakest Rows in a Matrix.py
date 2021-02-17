'''
1337. The K Weakest Rows in a Matrix
Problem Link : https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
Runtime: 84 ms
Memory Usage: 13.8 MB
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        dict={}
        for i in range(len(mat)):
            ans=sum(mat[i])
            dict[i]=ans
        l=sorted(dict.values())
        ans=[]
        for i in l[:k]:
            ans.append(dict.keys()[dict.values().index(i)])
            dict.pop(dict.keys()[dict.values().index(i)])
        return ans[:k]