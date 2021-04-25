class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        
        # A == B condition
        if a == b and len(set(a)) < len(a):
            return True
        else:    
                cnt=0

                index=[]
                for i in range(len(a)):
                    if a[i]!=b[i]:
                        index.append(i)
                        cnt+=1
                if cnt!=2:
                    return False
                else:
                    if len(index)==0:
                        return False
                    elif (a[index[0]]==b[index[1]] and a[index[1]]==b[index[0]]):
                            return True

