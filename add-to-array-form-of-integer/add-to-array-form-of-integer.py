class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp=[str(i) for i in num]
        temp=int(''.join(temp))
        temp=temp+k

        ls=[]
        
        if (temp==0):
            return [0]
        while temp!=0:
            t=temp%10
            ls.append(t)
            temp=temp//10
            
        return ls[::-1]
