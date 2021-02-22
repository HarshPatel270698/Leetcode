'''
991. Broken Calculator
Problem Link : https://leetcode.com/problems/broken-calculator
Runtime: 20 ms
Memory Usage: 13.7 MB
'''
class Solution(object):
    def brokenCalc(self, X, Y):
        loop=0
        while X<Y:
            if Y%2!=0:
                Y+=1
                loop+=1
            Y/=2
            loop+=1
        return loop+X-Y
'''
Runtime: 20 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def brokenCalc(self, X, Y):
        loop=0
        if X<=Y:
            while X<Y:
                if Y%2==0:
                    Y/=2
                    loop+=1
                else:
                    Y+=1
                    Y/=2
                    loop+=2
            if X>Y:
                loop+=X-Y
        elif X>Y:
            return X-Y
        return loop