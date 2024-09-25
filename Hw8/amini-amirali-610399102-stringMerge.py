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
a=list(input())
if len (a)!= 0:a=(srt(a))
b=list(input())
if len (b)!=0:b=srt(b)
a=a+b
for i in a :
    print (i,end='')
if len(a)==0:print ('')