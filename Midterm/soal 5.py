n = int(input())
m= [[x for x in list(map(int,input().split()))]for _ in range (n)]
list=[]
for i in range (len(m)):
    max=[0,m[i][0]]
    for y in range (1,len(m[i])):
        if m[i][y]>max[1]:
            max[0]=y
            max[1]=m[i][y]
    list.append(max[0])
for i in range (n):
    t=0
    for y in range (n):
        if (m[y][list[i]]>=m[i][list[i]]) and (y!=i):
            t=1
            break
    if t ==0 :print (i,list[i])