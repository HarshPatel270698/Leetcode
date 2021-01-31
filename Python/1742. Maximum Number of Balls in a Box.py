'''
1742. Maximum Number of Balls in a Box
Problem Link : https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
Runtime: 696 ms
Memory Usage: 16.2 MB
'''
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        dict={}
        sum=0
        for i in range(lowLimit,highLimit+1):
            k=i
            while k>0:
                temp=k%10
                sum+=temp
                k/=10
            if sum in dict.keys():
                add1=dict[sum]
                dict[sum]=add1+1
                add1=0
            else:
                dict[sum]=1
            sum=0
        return max(dict.values())