'''
413. Arithmetic Slices
Problem Link : https://leetcode.com/problems/arithmetic-slices/
Runtime: 168 ms
Memory Usage: 14 MB
'''
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        l,ans=len(A),0
        for i in range(l-2):
            d=A[i+1]-A[i]
            for j in range(i+2,l):
                if A[j]-A[j-1]==d:
                    ans+=1
                else:
                    break
        return ans