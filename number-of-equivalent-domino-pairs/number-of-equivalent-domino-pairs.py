class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen=[]
        for i in dominoes:
            i=sorted(i)
            seen.append(i[0]*10+i[1])

        h_s={}
        for i,v in enumerate(seen):
            if v in h_s:
                h_s[v]=h_s[v]+1
            else:
                h_s[v]=1
        return sum([v*(v-1)//2 for v in h_s.values()])
        