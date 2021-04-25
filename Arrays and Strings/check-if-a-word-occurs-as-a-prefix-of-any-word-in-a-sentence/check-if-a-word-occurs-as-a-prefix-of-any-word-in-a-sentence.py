class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent_list=sentence.split(" ")
        h={}
        for i,v in enumerate(sent_list):
            if v.startswith(searchWord):
                h[i]=v
        
        if len(h)==0:
            return '-1'
        else:
            return min(h.keys())+1
        