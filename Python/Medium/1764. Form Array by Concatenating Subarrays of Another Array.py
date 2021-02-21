'''
1764. Form Array by Concatenating Subarrays of Another Array
Problem Link : 
Runtime: 72 ms
Memory Usage: 13.9 MB
'''
class Solution(object):
    def canChoose(self, groups, nums):
        n,count,gn=str(nums)[1:-1],0,len(groups)
        for i in range(gn):
            s=str(groups[i])[1:-1]
            if s in n:
                count+=1
                n=''+n[n.index(s)+len(groups[i])+4:]
        return gn==count