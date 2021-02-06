'''
507. Perfect Number
Problem Link : https://leetcode.com/problems/perfect-number/
Runtime: 24 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def checkPerfectNumber(self, num):
        if num==1:
            return False
        s=set([1])
        for i in range(2,int(sqrt(num))+1):
            if num%i==0:
                s.add(i)
                s.add(num/i)
        return sum(s)==num
'''
Runtime: 16 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def checkPerfectNumber(self, num):
        return num in (6, 28, 496, 8128, 33550336)