'''
637. Average of Levels in Binary Tree
Problem Link : https://leetcode.com/problems/average-of-levels-in-binary-tree 
Runtime: 28 ms
Memory Usage: 18 MB
'''
class Solution(object):
    def averageOfLevels(self, root):
        res=[root.val]
        level=[root]
        while level:
            new_level=[]
            s = 0.0
            for node in level:
                if node.left:
                    new_level.append(node.left)
                    s+=node.left.val
                if node.right:
                    new_level.append(node.right)
                    s+=node.right.val
            if new_level:
                res.append(s/len(new_level))
            level=new_level
        return res