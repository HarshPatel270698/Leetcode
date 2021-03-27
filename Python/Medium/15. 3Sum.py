'''
15. 3Sum
Problem Link : https://leetcode.com/problems/3sum/
Runtime: 572 ms, faster than 90.57% of Python online submissions for 3Sum.
Memory Usage: 17.1 MB, less than 27.15% of Python online submissions for 3Sum.
'''
class Solution(object):
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        negatives,zeros,positives,ans=[],[],[],set()
        for i in nums:
            if i<0:
                negatives.append(i)
            elif i>0:
                positives.append(i)
            else:
                zeros.append(i)
        n=set(negatives)
        p=set(positives)
        if len(zeros)>=3:
            ans.add((0,0,0))
        if zeros:
            for i in n:
                if -1*i in p:
                    ans.add((-1*i,0,i))
        for i in range(len(negatives)):
            for j in range(i+1,len(negatives)):
                aim=abs(negatives[i]+negatives[j])
                if aim in p:
                    ans.add(tuple(sorted([negatives[i],negatives[j],aim])))
        for i in range(len(positives)):
            for j in range(i+1,len(positives)):
                aim=positives[i]+positives[j]
                if -1*aim in n:
                    ans.add(tuple(sorted([positives[i],positives[j],-1*aim])))
        return ans