'''
728. Self Dividing Numbers
Problem Link : https://leetcode.com/problems/self-dividing-numbers/
Runtime: 52 ms
Memory Usage: 13.7 MB
'''
class Solution(object):
    def selfDividingNumbers(self, left, right):
        a=[]
        c=0
        for i in range(left,right+1):
            t=str(i)
            for j in range(len(t)):
                if int(t[j])==0 or i%int(t[j])!=0:
                    c+=1
                    break
            if c==0:
                a.append(i)
            else:
                c=0
        return a