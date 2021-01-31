'''
859. Buddy Strings
Problem Link : https://leetcode.com/problems/buddy-strings/
Runtime: 52ms
Memory Usage: 14.5 MB
'''
class Solution(object):
    def buddyStrings(self, A, B):
        c=0
        s=0
        dicts={}
        dictd={}
        k=False
        d=0
        if len(A)!=len(B):
            return False
        for i in range(len(A)):
            if A[i]!=B[i]:
                c+=1
                if(dictd.get(A[i])):
                    if B[i]==dictd[A[i]]:
                        d+=1    
                else:   
                    dictd[A[i]]=B[i]
            if A[i]==B[i]:
                if (dicts.get(A[i])):
                    k= True
                else:
                    dicts[A[i]]=B[i]
                s+=1
        if(A==B and len(A)>1 and s>1 and k==True):
            return True
        elif c>2:
            return False
        elif len(dictd)>=2:
            if len(dictd)==2:
                l1= list(dictd.keys())[0]
                l2= list(dictd.keys())[1]
                right= dictd[l2]+dictd[l1]
                if (l1+l2)==right:
                    return True
                else:
                    return False
            else:
                return False
        elif c==2:
            if d<1:
                return True
            else:
                return False
        else:
            False