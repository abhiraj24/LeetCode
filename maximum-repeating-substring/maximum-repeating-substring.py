class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
                w=word
                i=0
                while i>=0:
                    if w in sequence:
                        i+=1
                        w=word*i
                
                    else:
                        break
                return i-1 if i>0 else 0
    
        