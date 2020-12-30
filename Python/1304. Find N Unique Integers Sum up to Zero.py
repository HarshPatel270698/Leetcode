'''
1304. Find N Unique Integers Sum up to Zero
Problem Link : https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
Runtime: 16 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def sumZero(self, n):
        a=[]
        if n%2==0:
            for i in range(1,n/2+1):
                a.append(i)
                a.append(-i)
        else:
            for i in range(1,n/2+1):
                a.append(i)
                a.append(-i)
            a.append(0)
        return a