'''
441. Arranging Coins
Problem Link : https://leetcode.com/problems/arranging-coins
Runtime: 960 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def arrangeCoins(self, n):
        count=0
        i=1
        while i<=n:
            count+=1
            n-=1
            i+=count
        return count