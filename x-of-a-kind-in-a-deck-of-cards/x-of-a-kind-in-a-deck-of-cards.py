class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        h={}
#s=[1,1,1,2,2,2,2]
#h={}
        for i,v in enumerate(deck):
                if v in h:
                    h[v]=h[v]+1
                else:
                    h[v]=1
            
        val_set=[v for k,v in h.items()]
            
        import functools as f
        #A = [12, 24, 27, 30, 36]
        g = lambda a,b:a if b==0 else g(b,a%b)   #Gcd for two numbers
        GCD=(f.reduce(lambda x,y:g(x,y),val_set)) 
        return GCD>1
        