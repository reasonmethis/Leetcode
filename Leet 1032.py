#https://leetcode.com/problems/stream-of-characters/
'''Runtime: 472 ms, faster than 96.06% of Python3 online submissions for Stream of Characters.
Memory Usage: 35.4 MB, less than 65.35% of Python3 online submissions for Stream of Characters.'''
#Pretty happy with the result. Before coming up with the tree approach was thinking of storing
#200 rolling hashes, one for each possible length of the suffix, updating them in constant time each
#and comparng each with a set of hashes for the words, also const t each, overall each query would 
#also b O(200 = max word length). But was concerned about collisions

#Clever code for building trie I found when was comparing my solution to others':
#(https://leetcode.com/problems/stream-of-characters/discuss/278250/Python-Trie-Solution-with-Explanation)
        # T = lambda: collections.defaultdict(T)
        # self.trie = T()
        # for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
class StreamChecker:
    def __init__(self, words: list[str]):
        self.stream = []
        self.maxlenwrd = 200 #max(words, key=len)
        self.maxlenstream = 10 * self.maxlenwrd
        #let's build a search tree starting from last chars of words
        #then we can find if any suffix of our stream is in the tree in O(max len of a word)
        self.rootdict = {}
        for word in words:
            curdict = self.rootdict
            for c in reversed(word):
                try:
                    curdict = curdict[c]
                except KeyError:
                    curdict[c] = {}
                    curdict = curdict[c]
            curdict['.'] = None #If '.' is in dict corresponding to path 'tac' that means 'cat' is in words

    def query(self, letter: str) -> bool:
        #first update stream
        self.stream.append(letter)
        if len(self.stream) == self.maxlenstream:
            self.stream = self.stream[-self.maxlenwrd:]

        #now do the tree search 
        curdict = self.rootdict
        for c in reversed(self.stream):
            try:
                curdict = curdict[c] #go to the node of the tree corresp to suffix c..end of stream
            except KeyError:
                return False
            if '.' in curdict:
                return True
        return False
