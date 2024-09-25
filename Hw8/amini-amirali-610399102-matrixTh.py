n=int(input())
mtrx=[[x for x in list(map(int , input().split()))]for _ in range (n)]
find = int(input())
f=True
for i in range (n):
    for y in range (n):
        if find ==mtrx[i][y]:
            print (i,y)
            f=False
if f == True:print ('NF')
