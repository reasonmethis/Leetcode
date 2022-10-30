#https://leetcode.com/problems/reverse-nodes-in-k-group/
'''Runtime: 96 ms, faster than 54.01% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.2 MB, less than 39.92% of Python3 online submissions for Reverse Nodes in k-Group.'''
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_next_k(node, fathernode, k):
            n_done = 0
            prevnode, curnode = None, node
            while n_done < k and curnode:
                childnode = curnode.next
                curnode.next = prevnode
                prevnode = curnode
                curnode = childnode
                n_done += 1
                
            #connect the newly reversed chain to the rest of the list
            node.next = curnode #original node connects at the tail now
            if fathernode:
                fathernode.next = prevnode 
                #fathernode now points to formerly last node in the group,
                #which is now its head
            return n_done, prevnode 
        
        grouphead, fathernode, finalglobalhead = head, None, None
        while grouphead:
            n_done, new_grouphead = reverse_next_k(grouphead, fathernode, k)
            if n_done < k:
                #restore the original order of the last group if it's short
                #we do this instead of storing the original order to have O(1) mem
                _, new_grouphead = reverse_next_k(new_grouphead, fathernode, n_done)
                return finalglobalhead or new_grouphead

            fathernode = grouphead #which is now last in group
            grouphead = grouphead.next
            finalglobalhead = finalglobalhead or new_grouphead #will assign only once, after first group
        return finalglobalhead


        
        