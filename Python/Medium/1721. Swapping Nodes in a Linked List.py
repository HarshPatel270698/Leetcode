'''
1721. Swapping Nodes in a Linked List
Problem Link : https://leetcode.com/problems/swapping-nodes-in-a-linked-list
Runtime: 1836 ms
Memory Usage: 90.3 MB
'''
class Solution(object):
    def swapNodes(self, head, k):
        l,s,e,c=0,0,0,0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        l-=k-1
        if k==l:
            return head
        temp=head
        while temp:
            c+=1
            if c==k:
                s=temp.val
            if c==l:
                e=temp.val
            temp=temp.next
        c=0
        temp=head
        while temp:
            c+=1
            if c==k:
                temp.val=e
            if c==l:
                temp.val=s
            print temp.val
            temp=temp.next
        return head