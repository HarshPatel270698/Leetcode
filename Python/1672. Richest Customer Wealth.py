'''
1672. Richest Customer Wealth
Problem Link : https://leetcode.com/problems/richest-customer-wealth/
Runtime: 36 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def maximumWealth(self, accounts):
        a=[]
        for i in range(len(accounts)):
            a.append(sum(accounts[i]))
        return max(a)