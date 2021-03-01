'''
575. Distribute Candies
Problem Link :https://leetcode.com/problems/distribute-candies/ 
Runtime: 684 ms
Memory Usage: 15.5 MB
'''
class Solution(object):
    def distributeCandies(self, candyType):
        l,s=len(candyType),set(candyType)
        sl=len(s)
        return min(l/2,sl)