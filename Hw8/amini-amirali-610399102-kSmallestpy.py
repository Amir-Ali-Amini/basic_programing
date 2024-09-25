def srt(x):
    x=list(map(int,x))
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
p=srt(list(map(int , input().split())))
d =int(input())
z=[p[0]]
for i in range (len (p)-1):
    if p[i+1]!=p[i]:z.append (p[i+1])
if d <= len (z) :print (z[d-1])
else : print ('NF')