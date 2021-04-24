class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<2:
            return 0
        
        prime=[True]*n
        prime[0]=False
        prime[1]=False

        for i in range(2,n):
            if prime[i]==True:
                for j in range(i+i,n,i):
                    prime[j]=False
        
        return sum(prime)
        