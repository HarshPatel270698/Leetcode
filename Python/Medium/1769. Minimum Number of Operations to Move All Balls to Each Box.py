'''
1769. Minimum Number of Operations to Move All Balls to Each Box
Problem Link : 
Runtime: 5052 ms
Memory Usage: 13.8 MB
'''
class Solution(object):
    def minOperations(self, boxes):
        ans=[]
        l=len(boxes)
        for i in range(l):
            count=0
            for j in range(l):
                if boxes[j]=="1":
                    if i>j:
                        count+=(i-j)
                    else:
                        count+=(j-i)
            ans.append(count)
        return ans