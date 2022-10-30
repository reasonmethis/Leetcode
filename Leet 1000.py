#https://leetcode.com/problems/minimum-cost-to-merge-stones/
'''Runtime: 89 ms, faster than 69.79% of Python3 online submissions for Minimum Cost to Merge Stones.
Memory Usage: 13.9 MB, less than 97.07% of Python3 online submissions for Minimum Cost to Merge Stones.'''
class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        #if we reverse the process, then at each step we are splitting one of the numbers into 
        #k "branches" that don't interact anymore. At the end we end up with the original n
        #numbers being split into k independent groups. Each group must contain (k-1)*integer + 1 
        #numbers, in order for it to be able to be merged into one number.
        #so, for example, the leftmost group must be of size x = 1, k, k + k-1, etc.
        #So if we know the answer to smaller problems we can loop over possible 
        #size x for the leftmost group and find the minimum of:
        #best cost to maximally reduce the leftmost x numbers PLUS 
        #best cost to maximally reduce the remaining n-x numbers (reduce to k-1 numbers)
        #which means we would need to maintain a table:
        #dp[i][p] = best cost to maximally reduce p numbers from index i,
        #where i ranges from 0 to n-1
        #So
        #dp[a][p] = min(dp[a][1] + dp[a+1][p-1], dp[a][k] + dp[a+k][p-k],...) + cost of final merge if can
        n = len(stones)
        if k != 2 and n % (k - 1) != 1:
            return -1
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        #build prefix sum array. prefsum[i] will contain the sum of the first i stones
        prefsum = [0]
        for val in stones:
            prefsum.append(prefsum[-1] + val)

        for p in range(k, n + 1):
            for i in range(n - p + 1):
                mincost = float('inf')
                for leftgroupsize in range(1, p, k - 1):
                    mincost = min(mincost, dp[i][leftgroupsize] + dp[i + leftgroupsize][p - leftgroupsize])
                dp[i][p] = mincost + prefsum[i + p] - prefsum[i] if k == 2 or p % (k - 1 ) == 1 else mincost

        return dp

print(Solution().mergeStones([3, 2, 4, 1], 2))
