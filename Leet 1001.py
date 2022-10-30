#https://leetcode.com/problems/grid-illumination/
'''Runtime: 1887 ms, faster than 67.74% of Python3 online submissions for Grid Illumination.
Memory Usage: 46.7 MB, less than 8.60% of Python3 online submissions for Grid Illumination.'''
#Reading other solutions: can just store number of lamps in a given row instead of set of cols, etc
class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        occrows, occcols, occdiagp, occdiagm = {}, {}, {}, {}
        for row, col in lamps:
            try:
                occrows[row].add(col)
            except KeyError:
                occrows[row] = {col}
            try:
                occcols[col].add(row)
            except KeyError:
                occcols[col] = {row}
            try:
                occdiagp[row + col].add((row, col))
            except KeyError:
                occdiagp[row + col] = {(row, col)}
            try:
                occdiagm[row - col].add((row, col))
            except KeyError:
                occdiagm[row - col] = {(row, col)}

        ans = []
        for row, col in queries:
            plu, mns = row + col, row - col
            ans.append(1 if row in occrows or col in occcols or plu in occdiagp or mns in occdiagm else 0)

            for r in range(max(0, row - 1), min(n, row + 2)):
                for c in range(max(0, col - 1), min(n, col + 2)):
                    try:
                        occrows[r].remove(c)
                        if not occrows[r]:
                            del occrows[r]
                    except Exception:
                        pass
                    try:
                        occcols[c].remove(r)
                        if not occcols[c]:
                            del occcols[c]
                    except Exception:
                        pass
                    try:
                        occdiagp[r + c].remove((r, c))
                        if not occdiagp[r + c]:
                            del occdiagp[r + c]
                    except Exception:
                        pass
                    try:
                        occdiagm[r - c].remove((r, c))
                        if not occdiagm[r - c]:
                            del occdiagm[r - c]
                    except Exception:
                        pass

        return ans

print(Solution().gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,0]]))
            
        