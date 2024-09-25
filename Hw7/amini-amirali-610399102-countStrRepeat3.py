def srt(x):
    if len (x)==1:
        return x
    first_half=srt(x[:len(x)//2])
    seccend_half=srt(x[len(x)//2:])
    count_first_half=count_seccend_half=0
    d=[]
    while ((count_first_half<len(first_half))or (count_seccend_half<len(seccend_half))):
        if count_first_half==len(first_half):
            d.append(seccend_half[count_seccend_half])
            count_seccend_half+=1
        elif count_seccend_half==len(seccend_half):
            d.append(first_half[count_first_half])
            count_first_half+=1
        else :
            if seccend_half[count_seccend_half]>first_half[count_first_half]:
                d.append(first_half[count_first_half])
                count_first_half+=1
            else :
                d.append(seccend_half[count_seccend_half])
                count_seccend_half+=1
    return d
def reverse(x):
    d=[]
    for q in range(len(x)-1,-1,-1):
        d.append(x[q])
    return d
n=input()
if len(n)==2:
    print (n,1)
else:
    duplex=[n[x:x+2]for x in range (len(n)-1)if (n[x]!=' ')and(n[x+1]!=' ')]
    if len(duplex)>0:
        duplex=srt(duplex)
        i=1
        counter=[]
        while(len(duplex)>0):
            if len(duplex)==1:
                counter+=[[len(duplex[:i]),duplex[0]]]
                del(duplex[:i])
                break
            elif duplex[i]==duplex[0]:
                i+=1
                if i==len(duplex):
                    counter+=[[len(duplex[:i]),duplex[0]]]
                    del(duplex[:i])
                    break
            else:
                counter+=[[len(duplex[:i]),duplex[0]]]
                del(duplex[:i])
                i=1
                if len(duplex)==1:
                    counter+=[[len(duplex[:i]),duplex[0]]]
                    del(duplex[:i])
        counter=reverse(srt(counter))
        i,j=1,0
        if len(counter)>1:
            while j<len(counter):
                if counter[i][0]==counter[j][0]:
                    i+=1
                    if(i==len(counter)):
                        d=counter[j:i]
                        d=srt(d)
                        counter[j:i]=d
                        break
                else:
                    d=counter[j:i]
                    d=srt(d)
                    counter[j:i]=d
                    j=i
        for i in counter:
            print (i[1],i[0])