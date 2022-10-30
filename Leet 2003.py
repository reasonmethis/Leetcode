#https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/
'''Runtime: 7752 ms, faster than 5.61% of Python3 online submissions for Smallest Missing Genetic Value in Each Subtree.
Memory Usage: 64.3 MB, less than 51.40% of Python3 online submissions for Smallest Missing Genetic Value in Each Subtree.'''
#Slow for some reason. Complexity should be n log n: n log n preprocessing to build the bin lifting
#table, then we go through each val 1..n and find lca in log n, so should be another factor of n log n

#Oh, looking in the discussion section I see that there's a linear time solution. Before reading the answers:
#I guess we can actually find where nodes with val = 2, 3,... connect to the main chain (node with val = 1 
#and its ancestors - the only nodes with non-1 answers) in linear time, we don't need all that binary
#lifting stuff: just go through each node X on the main chain, do dfs on all its other children and for each 
#node store connection_to_main_chain[val in that node] = X. Finish that table by going through the main chain,
#and then use it: set answer to 2 for all nodes between val=1 node and connection_to_main_chain[val=2], 
#excluding the latter, then set answer to 3 for all nodes between the latter and 
#connection_to_main_chain[val=3], excluding that last node, etc

class Solution:
    def smallestMissingValueSubtree(self, parents: list[int], nums: list[int]) -> list[int]:
        def lift_by_k(node, k): #O(log n)
            if depth[node] < k:
                return -1
            k_remaining = k
            exponent = LOG - 1
            power_of_2 = 2 ** exponent
            while k_remaining:
                if k_remaining >= power_of_2:
                    node = up[exponent][node]
                    k_remaining -= power_of_2
                exponent -= 1
                power_of_2 = power_of_2 // 2 #speed up with bitshifts?
            return node

        def get_lca(node1, node2): #O(log n)
            #equalize depths
            d_depth = depth[node2] - depth[node1]
            if d_depth > 0:
                node2 = lift_by_k(node2, d_depth)
            else:
                node1 = lift_by_k(node1, -d_depth)
            if node1 == node2:
                return node1

            #now basically binary search to find lca
            exponent, poss_depth, common_depth = -1, 1, depth[node1]
            ##if for ex common depth is 2 or 3 I should start with exponent 1 (check grandparents)
            while poss_depth <= common_depth: 
                exponent += 1
                poss_depth *= 2
            while parents[node1] != parents[node2]:
                if exponent == 0:
                    u=5
                liftednode1, liftednode2 = up[exponent][node1], up[exponent][node2]
                if liftednode1 != liftednode2:
                    node1, node2 = liftednode1, liftednode2
                exponent -= 1
            return parents[node1]            

        #initialize vars and calculate log of n
        tmp = n = len(nums)
        LOG = 1
        while tmp > 1:
            tmp = tmp // 2
            LOG += 1
        children = [[] for _ in range(n)]
        val2ind = {}
        #up[k][i] will be 2**k-th ancestor of node i
        #this is binary lifting: https://www.youtube.com/watch?v=oib-XsjFa-M
        up = [[0] * n for _ in range(LOG)] 

        #get children info, lookup table for values, first row of up table
        for i, (parent, val) in enumerate(zip(parents, nums)):
            val2ind[val] = i
            if parent >= 0: 
                children[parent].append(i) 
                up[0][i] = parent 
            else: 
                #keep up[1][root] at root, otherwise dp below will be trickier 
                up[0][i] = i #don't need that for this specific problem cuz 0=root

        #dfs to get depths
        depth = [0] * n
        to_visit = [0] #NOTE in the general case this would be root instead of 0
        while to_visit:
            curnode = to_visit.pop()
            childrensdepth = depth[curnode] + 1
            for child in children[curnode]:
                depth[child] = childrensdepth
            to_visit.extend(children[curnode])

        #build the up table row by row, O(n log n)
        for k in range(1, LOG): 
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]] #that's why we wanted up[1][root] == root

        #EVERYTHING SO FAR HAS BEEN PRETTY GENERAL, WE HAVE IMPLEMENTED EFFICIENT LIFTING AND LCA
        #Now let's use it to find the answer to our problem 
        minmissing = [1] * n
        #find node with value 1, only it and its ancestors have non-1 answers
        try:
            node_oi = val2ind[1]
        except KeyError:
            return minmissing

        #now find lca of node_oi and node with value val=2, set answers for node_oi, its parent,
        #its grandparent etc up to (but not including) that lca to 2
        #then find lca of that lca and node with val=3, etc etc etc
        val = 2
        while node_oi != -1:
            try:
                lca = get_lca(node_oi, val2ind[val])         
            except KeyError:
                lca = -1   
            while node_oi != lca:
                minmissing[node_oi] = val
                node_oi = parents[node_oi]
            val += 1

        return minmissing

'''import random
for i in range(1000000):
    n = random.randint(1, 20)
    parents = [-1] + 
    nums = [221,2,3,1,9,6,8,7,4]
print(Solution().smallestMissingValueSubtree(parents, nums))'''
