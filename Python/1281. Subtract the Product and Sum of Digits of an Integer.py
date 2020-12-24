'''
1281. Subtract the Product and Sum of Digits of an Integer
Problem Link : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Runtime: 8 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def subtractProductAndSum(self, n):
        m=1
        s=0
        a=list(str(n))
        for i in range(len(a)):
            m*=int(a[i])
            s+=int(a[i])
        return m-s