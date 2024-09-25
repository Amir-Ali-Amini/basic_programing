ls=[[]]
for i in range (int(input())):
    lsi=[]
    for j in ls:
        lsi.append(j+[i+1])
        for t in (j+[i+1]):print (t,end=' ')
        print ()
    ls+=lsi
'''for i in ls:
    if i!=[]:
        for j in i:
            print (j,end=' ')
    print ()'''