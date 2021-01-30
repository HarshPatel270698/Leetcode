'''
7.reverse-integer
Problem Link : https://leetcode.com/problems/reverse-integer
Runtime: 8 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def reverse(self, x):
        if x==0:
            return x
        else:
                ans=""
                c=0
                x=str(x)
                x=x[::-1]
                for i in x:
                    if c==0 and i=='0':
                        continue
                    elif i=='-':
                        ans='-'+ans
                        break
                    else:
                        c+=1
                        ans+=str(i)
        if -2**31<=int(ans)<=2**31-1:
            return ans
        else:
            return 0

