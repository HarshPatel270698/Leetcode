'''
11. Container With Most Water
Problem Link : https://leetcode.com/problems/container-with-most-water
Runtime: 136 ms
Memory Usage: 15.2 MB
'''
class Solution(object):
    def maxArea(self, height):
        ans,i,j=0,0,len(height)-1
        while (i<j):
            ans=max(ans,(min(height[i],height[j])*abs(j-i)))
            if height[i]>height[j]:
                j-=1
            else: 
                i+=1
        return ans
'''
TLE using Brute Force, works with python
'''
class Solution(object):
    def maxArea(self, height):
        s,l=0,len(height)
        for i in range(1,l):
            for j in range(i,l):
                s=max(s,(min(height[i-1],height[j])*abs(i-j-1)))
        return s