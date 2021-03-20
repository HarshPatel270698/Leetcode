'''
1796. Second Largest Digit in a String
Problem Link : https://leetcode.com/problems/second-largest-digit-in-a-string/
Runtime: 16 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def secondHighest(self, s):
        m=ans=-1 #m is biggest number ans is second biggest number
        for i in s:
            if i.isdigit(): #if it's number
                if i>m: #number is greater than biggest number
                    ans=m #as old biggest number became scond biggest number set ans as second biggest number
                    m=i #set new number as biggest number
                if m>i>ans: #if number is not the most biggest number but bigger than second biggest
                    ans=i #set number as second biggest number
        return ans
#To make it short:

class Solution(object):
    def secondHighest(self, s):
        m=ans=-1
        for i in s:
            if i.isdigit():
                if i>m:ans,m=m,i
                if m>i>ans:ans=i
        return ans