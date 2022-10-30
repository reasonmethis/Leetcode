#https://leetcode.com/problems/merge-k-sorted-lists/
'''Runtime: 111 ms, faster than 91.85% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.6 MB, less than 13.84% of Python3 online submissions for Merge k Sorted Lists.'''
from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_rootnode = None
        #create a min heap out of initial root nodes,
        #then keep popping the smallest item (O(log k))
        #and replacing it with its successor (O(log k))
        #that way finding the min of the current candidates is log instead of linear 
        nodesheap = [(node.val, tiebreaker, node.next) for tiebreaker, node in enumerate(lists) if node]
        #include unique tiebreaker numbers to avoid comparing ListNodes:
        #see https://docs.python.org/3/library/heapq.html
        heapq.heapify(nodesheap)
        while nodesheap:
            minval, tiebreaker, childnode = heapq.heappop(nodesheap)
            my_newnode = ListNode(val=minval)
            if my_rootnode:
                my_curnode.next = my_newnode
                my_curnode = my_newnode
            else: #first one
                my_rootnode = my_curnode = my_newnode
            if childnode:
                heapq.heappush(nodesheap, (childnode.val, tiebreaker, childnode.next))
        return my_rootnode

