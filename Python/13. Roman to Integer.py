'''
13. Roman to Integer
Problem Link : https://leetcode.com/problems/roman-to-integer
Runtime: 32 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def romanToInt(self, s):
        dict,ans={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        },0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(dict.get, s))