#https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
'''Runtime: 109 ms, faster than 78.16% of Python3 online submissions for Recover a Tree From Preorder Traversal.
Memory Usage: 14.8 MB, less than 28.16% of Python3 online submissions for Recover a Tree From Preorder Traversal.'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        toks = traversal.split('-')
        parents = [TreeNode()] #dummy root
        depth = 1 #will be the intended depth of each integer token in the tree rel to dummy root
        for tok in toks:
            if not tok: #means there were at least two dashes in a row, so depth >= 3
                depth += 1
                continue
            n_to_pop = len(parents) - depth
            if n_to_pop > 0:
                del parents[-n_to_pop:]
            parent = parents[-1]
            newnode = TreeNode(int(tok))
            if parent.left:
                parent.right = newnode
            else:
                parent.left = newnode
            parents.append(newnode)
            depth = 2
        return parents[1]

            
