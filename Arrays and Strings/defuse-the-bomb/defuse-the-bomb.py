class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
            if k>0:
                res=[]
                code=code+code[0:k]
                for i in range(1,len(code)-k+1):
                    res.append(sum(code[i:i+k]))
            elif k<0:
                res=[]
                code=code[len(code)-abs(k):len(code)]+code
                for i in range(0,len(code)+k):
                    res.append(sum(code[i:i-k]))
                    
            elif k==0:
                res=[]
                for i in range(0,len(code)):
                    res.append(0)
            return res