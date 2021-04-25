class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B=sorted(A)
        C=B[::-1]
#print(A)
#print(B)
#print(C)


        if(A==B) or (A==C):
            return True
        else:
            return False
    