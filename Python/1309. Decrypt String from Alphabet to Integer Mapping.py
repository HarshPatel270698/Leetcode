'''
1309. Decrypt String from Alphabet to Integer Mapping
Problem Link : https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
Runtime: 20 ms
Memory Usage: 13.5 MB
'''
class Solution(object):
    def freqAlphabets(self, s):
        dict={}
        c=0
        a=''
        for i in range(65,91):
            if i>73:
                dict[str(i-64)+'#']=chr(i).lower()
            else:    
                dict[str(i-64)]=chr(i).lower()
        for i in range(len(s)-2):
            if c==0:
                if s[i+2]=='#':
                    a+=dict[s[i:i+3]]
                    c+=2
                else:
                    a+=dict[s[i]]
            else:
                c-=1
        if s[len(s)-1]!='#':
            if s[len(s)-2]=='#':
                a+=dict[s[len(s)-1]]
            else:
                a+=dict[s[len(s)-2]]
                a+=dict[s[len(s)-1]]
        return a