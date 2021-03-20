'''
1798. Maximum Number of Consecutive Values You Can Make
Problem Link : https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
Runtime: 784 ms
Memory Usage: 17.4 MB
'''
class Solution(object):
    def getMaximumConsecutive(self, coins):
        ans=1
        for i in sorted(coins):
            if i>ans:break
            ans+=i
        return ans