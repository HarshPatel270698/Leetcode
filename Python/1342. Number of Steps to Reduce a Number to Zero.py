'''
1342. Number of Steps to Reduce a Number to Zero
Problem Link : https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Runtime: 12 ms
Memory Usage: 13.6 MB
'''
class Solution(object):
    def numberOfSteps (self, num):
        i=0
        while(num>0):
            if(num%2==0):
                num=num/2
                i+=1
            else:
                num=num-1
                i+=1
        return i