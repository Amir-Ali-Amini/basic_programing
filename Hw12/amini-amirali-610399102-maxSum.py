ls=list(map(int,input().split()))
def chek(ls):
    if len (ls)==1:
        return ls
    else:
        td=ls[:]
        for i in range (len(ls)):
            if sum(ls[i:])>sum(td):
                td=ls[i:]
        c=(chek(ls[:-1]))
        if sum(c)>sum(td):return c
        else :return td
for i in  (chek(ls)):
    print (i , end=' ')