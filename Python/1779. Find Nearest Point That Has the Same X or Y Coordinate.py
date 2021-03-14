'''
1779. Find Nearest Point That Has the Same X or Y Coordinate
Problem Link : https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate
Runtime: 576 ms
Memory Usage: 18.6 MB
'''
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        count=0
        l=[]
        flag=True
        m=10000
        ind=0
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                flag=False
                temp=abs(x-points[i][0])+abs(y-points[i][1])
                l.append(temp)
                if m>temp:
                    m=temp
                    ind=i
        if len(l)==0:
            return -1
        return ind
'''        
Runtime: 932 ms
Memory Usage: 18.8 MB
'''
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        count=0
        l=[]
        flag=True
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                flag=False
                l.append(abs(x-points[i][0])+abs(y-points[i][1]))
        if len(l)==0:
            return -1
        m=min(l)
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                if m==abs(x-points[i][0])+abs(y-points[i][1]):
                    return i