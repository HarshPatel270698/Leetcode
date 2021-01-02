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
		
'''
Runtime: 16 ms
Memory Usage: 13.9 MB
'''
class Solution(object):
    def selfDividingNumbers(self, left, right):
        a=[]
        c=0
        for i in range(left,right+1):
            t=i
            while t>0:
                rem=t%10
                if rem==0 or i%rem!=0:
                    c+=1
                    break
                t//=10
            if c==0:
                a.append(i)
            else:
                c=0
        return a