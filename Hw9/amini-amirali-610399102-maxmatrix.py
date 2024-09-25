n,m=map(int,input().split())
matrix=[[x for x in list (map(int,input().split()))]for _ in range (n)]
sumi=0
mt=[]
max=0,0
for _ in range (n-m+1):
    mt.append([0]*(n-m+1))
for x in range (m):
    for y in range (m):
        sumi+=matrix[x][y]
sm=sumi
for x in range (n-m+1):
    for y in range (n-m+1):
        if (x==0) & (y==0) : mt[0][0]=sumi
        else:
            d=0
            dd=0
            if y!=0:
                for i in range (m):
                    d+= matrix[x+i][y-1]
                    dd +=matrix[x+i][y+m-1]
                mt[x][y]=mt[x][y-1]+dd-d
            else :
                for i in range (m):
                    d+= matrix[x-1][y+i]
                    dd +=matrix[x+m-1][y+i]
                mt[x][y]=mt[x-1][y]+dd-d
        if mt[x][y]>mt[max[0]][max[1]]:
            #print ('**')
            max=x,y
#for i in mt:print (i)
#print (max)
for x in range (m):
    for y in range (m):print (matrix[x+max[0]][y+max[1]],end=' ')
    print ()