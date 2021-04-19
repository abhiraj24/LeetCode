class Solution:
    def longestWord(self, words: List[str]) -> str:
        string_set=set()
        string_set.add('')
        s=sorted(words)
        size=0
        for word in s:
            if word[:-1] in string_set:
                if len(word)>size:
                    size=len(word)
                    ans=word
                string_set.add(word)
        return ans
        