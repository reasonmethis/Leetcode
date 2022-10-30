#https://leetcode.com/problems/numbers-with-repeated-digits/
'''Runtime: 65 ms, faster than 49.51% of Python3 online submissions for Numbers With Repeated Digits.
Memory Usage: 14 MB, less than 48.54% of Python3 online submissions for Numbers With Repeated Digits.'''
#I guess all that precomputing didn't help much
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        '''def precompute(ndigits, ndigits_avail):
            totdiff = 1
            for place in range(ndigits):
                totdiff *= ndigits_avail
                ndigits_avail -= 1
            return totdiff
        def print_answers_all_n_or_lower_digits(ndigitsmax=9):
            ans = [0]
            for ndigits in range(1, ndigitsmax + 1):
                ans.append(ans[-1])
                totdiff = ndigits_avail = 9
                for place in range(ndigits - 1):
                    totdiff *= ndigits_avail
                    ndigits_avail -= 1
                ans[-1] += totdiff
            print(ans)
        def print_full_precomp_table():
            tbl = []
            for ndigits in range(10):
                tbl.append([])
                for ndigits_avail in range(11):
                    tbl[-1].append(precompute(ndigits, ndigits_avail))
            import pprint
            #pprint.pprint(tbl)
            print(tbl)
        #print_full_precomp_table();exit()
        print_answers_all_n_or_lower_digits(); exit()'''
        precomputed = [[1] * 11, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 2, 6, 12, 20, 30, 42, 56, 72, 90], [0, 0, 0, 6, 24, 60, 120, 210, 336, 504, 720], [0, 0, 0, 0, 24, 120, 360, 840, 1680, 3024, 5040], [0, 0, 0, 0, 0, 120, 720, 2520, 6720, 15120, 30240], [0, 0, 0, 0, 0, 0, 720, 5040, 20160, 60480, 151200], [0, 0, 0, 0, 0, 0, 0, 5040, 40320, 181440, 604800], [0, 0, 0, 0, 0, 0, 0, 0, 40320, 362880, 1814400], [0, 0, 0, 0, 0, 0, 0, 0, 0, 362880, 3628800]]
        #fulldigitanswers = [0, 0, 9, 261, 4725, 67509, 831429, 9287109, 97654149, 994388229]
        fulldigitanswers = [0, 9, 90, 738, 5274, 32490, 168570, 712890, 2345850, 5611770]
        #precomputed[ndigits][navail] = how many ndigits-length seqs of digits there are with
        #no duplicate digits if only navail digits are "available" (10-navail already being used
        #so using one of them in the sequence counts as having a seq with duplicate digits)
        #fulldigitanswers[4] = how many numbers with no duplicate digits are there in [1, 9999]
        if n >= 987654321:
            return n - 5611770
        digits = []
        nn = n
        while n:
            n, dig = divmod(n, 10)
            digits.append(dig)
        ndigits, ndigits_avail = len(digits) - 2, 8
        firstdig = digits.pop()
        totdiff = fulldigitanswers[ndigits + 1] + (firstdig - 1) * precomputed[ndigits + 1][9]
        digits_sofar = {firstdig}
        #so far this counts all numbers wth smaller-digit numbers + all numbers where the first digit is
        #lower than the first digit in n
        for digit in reversed(digits):
            #now we count numbers with first digit same as in n, next digit lower than the next digit in n
            #then, on next loop iteration, count all nums with the first two digits same as in n but
            #next one lower, etc
            n_poss_lower_digits = len(set(range(digit)) - digits_sofar)
            totdiff += n_poss_lower_digits * precomputed[ndigits][ndigits_avail]
            if digit in digits_sofar:
                break
            digits_sofar.add(digit)
            ndigits -= 1
            ndigits_avail -= 1
        else:
            totdiff += 1 #all digits same as in n
        return nn - totdiff      

print(Solution().numDupDigitsAtMostN(20))
