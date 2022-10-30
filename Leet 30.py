#https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''Runtime: 528 ms, faster than 68.77% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.2 MB, less than 79.34% of Python3 online submissions for Substring with Concatenation of All Words.'''
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        stlen, n_words, wordlen = len(s), len(words), len(words[0])
        words_cntr= Counter(words)
        inds_found = []
        i_last = stlen - n_words * wordlen
        for i in range(max(i_last + 1, 0)):
            working_words_cntr = words_cntr.copy()
            #look for all words chunk by chunk
            for j in range(i, i + n_words * wordlen, wordlen):
                chunk = s[j:j + wordlen]
                if chunk not in working_words_cntr or working_words_cntr[chunk] == 0:
                    break #chunk not found 
                working_words_cntr[chunk] -= 1
            else: #all chunks found 
                inds_found.append(i)
        return inds_found