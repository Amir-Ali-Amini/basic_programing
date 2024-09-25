prime =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
n=int(input())
if n>1:
    ls=[]
    for i in range (2*n):
        ls.append([])
    ls[0]+=[[0]]
    for i in prime :
        if i<=n:
            for y in range (n):
                if i+y<=n:
                    if len(ls[y])!=0:
                        for q in ls[y]:
                            ls[y+i].append(q+[i])
    ls=sorted(ls[n])
    for i in ls:
        for t in i :
            if t!=0:print (t,end=' ')
        print ()