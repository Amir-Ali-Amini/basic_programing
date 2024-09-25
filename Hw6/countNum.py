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
input()
n=srt(list(map(int,input().split())))
i=0
counter=[]
z=0
while len(n)>0:
    if i==len(n):
        counter+=[[i,n[0]]]
        del(n[:i])
        i=0
    elif (n[0]==n[i])&(z!=1):
        i+=1
    else:
        counter+=[[i,n[0]]]
        del(n[:i])
        i=0
i=0

counter=srt(counter)
while 1:
    i-=1
    if i==-(len(counter)):
        break
    elif counter[i][0]!=counter[i-1][0] : break
print (counter[i][1])
