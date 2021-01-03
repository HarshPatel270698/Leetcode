'''
1450. Number of Students Doing Homework at a Given Time
Problem Link : https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
Runtime: 24 ms
Memory Usage: 13.2 MB
'''
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        a=0
        for i in range(len(endTime)):
            if endTime[i]>=queryTime:
                if startTime[i]<=queryTime:
                    a+=1
        return a
'''
Runtime: 16 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        a=0
        for s,e in zip(startTime, endTime):
            if s<=queryTime<=e:
                a+=1
        return a
