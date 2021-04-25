class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        h_s={}
        paragraph=paragraph.lower()
        alpha_num=re.findall('\w+',paragraph)
        para=[i for i in alpha_num if i not in '_' ]
        for i,v in enumerate(para):
            if v in h_s:
                h_s[v]=h_s[v]+1
            else:
                h_s[v]=1 
        
        unbanned={k:v for k,v in h_s.items() if k not in banned}
        max_value=max(unbanned.values())
        
        for k,v in unbanned.items():
            if v==max_value:
                return k
        
        
        