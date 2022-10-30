#https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        #the global index of the median element (or the first of the two) is ioi = (N - 1) // 2, call its value v
        #We can have an algorithm that finds elm with arbitrary global index i and use it to find that ioi elm.
        #So how to find elm with inde i? If it's in first array with index x and value v, then there 
        #are x elms to the left in nums1 and hence i - x elms should be "lefter" than v in the second array
        #so let's find x = number of elms in first array that are less than v
        m, n = len(nums1), len(nums2)
        #let's rename things to make first array >= in length than second array 
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        n_lefter_elms_globally = (m + n - 1) // 2 #what I called ioi, aka num of elms lefter than v globally

        #Looking for index x, aka num of lefter elms in just the first array 
        #Start with the lowest and highest possible candidates, then narrow down with binary search 
        x_low, x_high = max(n_lefter_elms_globally - n, 0), n_lefter_elms_globally 
        while x_high > x_low:
            x_mid = (x_high + x_low) // 2
            v = nums1[x_mid]
            n_lefter_elms_in_nums2 = n_lefter_elms_globally - x_mid
            if n_lefter_elms_in_nums2 and nums2[n_lefter_elms_in_nums2 - 1] > v: 
                #x_mid is too low - the rightmost elm in second array that was supposed to be lefter than
                #v is actually bigger than v
                x_low = x_mid + 1
            else:
                x_high = x_mid 
        v1 = nums1[x_high] #x_high = x_low = the x we were looking for 
        #now we have the smallest elm in first array such that the total number of lefter elms is at least 
        #n_lefter_elms_globally. But need to check if there's a smaller candidate in the second array 
        i_in_nums2_to_check = n_lefter_elms_globally - x_high
        if (m + n) % 2:
            #just return the single (N-2)//2-th element, the smaller of the two candidates (one from each array)
            return min(v1, nums2[i_in_nums2_to_check]) if i_in_nums2_to_check < n else v1

        #need to do more work, not just find that (N-2)//2-th element, but then also the next one, and avg them
        if i_in_nums2_to_check >= n: 
            #no candidates in second array 
            return (v1 + nums1[x_high + 1]) / 2

        v2 = nums2[i_in_nums2_to_check]
        if v1 < v2:
            v_next = min(v2, nums1[x_high + 1]) if x_high + 1 < m else v2
            return (v1 + v_next) / 2
        else:
            v_next = min(v1, nums2[i_in_nums2_to_check + 1]) if i_in_nums2_to_check + 1 < n else v1
            return (v2 + v_next) / 2
        
import random

for i in range(1000000):
    m = random.randint(1, 10)
    n = random.randint(0, 10)
    numsm = sorted([random.randint(-11, 15) for x in range(m)])
    numsn = sorted([random.randint(-10, 10) for x in range(n)])
    numsall = sorted(numsm + numsn)
    ans = numsall[(m + n - 1) // 2] if (m + n) % 2 else (numsall[(m + n - 1) // 2] + numsall[(m + n - 1) // 2 + 1]) / 2

    val = Solution().findMedianSortedArrays(numsm, numsn)
    if ans!= val:
        print(numsm)
        print(numsn)
        input(f'{i=} {ans=} {val=}')
    elif i % 1000 == 0:
        print(i)
i=1

