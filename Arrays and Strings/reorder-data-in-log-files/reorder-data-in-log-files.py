class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits=[]
        letters=[]
        for i in range(0,len(logs)):
            index_wh=logs[i].find(' ')
            #print(index_wh)
            if re.findall('\d',logs[i][index_wh+1]):
                digits.append(logs[i])
            else:
                letters.append(logs[i])
                
        letters.sort(key = lambda x: (x.split(' ',1)[1], x.split(' ',1)[0]))
        #letters+digits
                
        
        #dict_leters = {}
        #for i in letters:
        #    index=i.find(' ')
        #    key=i[:index]
        #    #dict_leters[key]=i[index:]
        #    dict_leters.setdefault(key, []).append(i[index:])
        #
        #dict_leters={k: v for k, v in sorted(dict_leters.items(), key=lambda item: item[1])}
        #dict_leters=sorted(dict_leters.items(), key=lambda t: t[::-1])
        #
        #result=[]
        #for i in dict_leters:
        #    if(len(i[1])==1):
        #        result.append(i[0]+','.join(i[1]))
        #    else:
        #        z=sorted(i[1])
        #        for k in range(len(z)):
        #            
        #            result.append(i[0]+z[k])
        #            
        return letters+digits