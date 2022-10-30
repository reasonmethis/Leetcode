#https://leetcode.com/problems/regular-expression-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.p_len = len(p)
        self.s_len = len(s)
        self.cache = {}
        return self._is_match(0, 0)

    def _is_match(self, s_ind, p_ind) -> bool:
        if p_ind == self.p_len:
            return s_ind == self.s_len
        try:
            return self.cache[(s_ind, p_ind)]
        except KeyError:
            pass
        c = self.p[p_ind]
        cnext = self.p[p_ind + 1] if p_ind + 1 < self.p_len else ''
        if cnext == '*':
            if c == '.':
                n_max_match = self.s_len - s_ind 
            else:
                n_max_match, ind = 0, s_ind
                while ind < self.s_len and self.s[ind] == c:
                    n_max_match += 1
                    ind += 1

            res = False
            for ind in range(s_ind, s_ind + n_max_match + 1):
                if self._is_match(ind, p_ind + 2):
                    res = True
                    break
        else:
            first_char_ismatch = s_ind < self.s_len and (c == '.' or c == self.s[s_ind])
            res = first_char_ismatch and self._is_match(s_ind + 1, p_ind + 1) 
        self.cache[(s_ind, p_ind)] = res
        return res

s = '28÷54h'
p = 'a*.*g*'
print(Solution().isMatch(s, p))
        