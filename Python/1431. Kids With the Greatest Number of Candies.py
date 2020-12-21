'''
1431. Kids With the Greatest Number of Candies
Problem Link : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Runtime: 32 ms
Memory Usage: 13.3 MB
'''
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=[]
        for i in range(len(candies)):
            sum = candies[i] + extraCandies
            if sum >= max(candies):
                a.append(True)
            else:
                a.append(False)
        return a