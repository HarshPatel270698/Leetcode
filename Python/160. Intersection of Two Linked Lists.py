'''
160. Intersection of Two Linked Lists
Problem Link : https://leetcode.com/problems/intersection-of-two-linked-lists/
Runtime: 172 ms
Memory Usage: 43.6 MB
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a = set()
        while headA is not None:
            a.add(headA)
            headA=headA.next
        while headB is not None:
            if headB in a:
                return headB
            headB=headB.next
        return None