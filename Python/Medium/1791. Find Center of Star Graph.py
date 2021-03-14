'''
1791. Find Center of Star Graph
Problem Link : https://leetcode.com/problems/find-center-of-star-graph
Runtime: 692 ms
Memory Usage: 52.5 MB
'''
class Solution(object):
    def findCenter(self, edges):
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            return edges[0][0]
        return edges[0][1]