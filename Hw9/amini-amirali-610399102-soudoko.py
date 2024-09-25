n=int(input())
matrix=[[x for x in list (map(int,input().split()))]for _ in range (n)]
lsx=[0]*(n+1)
lsy=[0]*(n+1)
z=True
for x in range (n):
    if z==True:
        for y in range (n):
            #print (x,y,matrix[x][y],matrix[y][x])
            if matrix[x][y]>n:
                print ("Not Valid")
                z=False
                break
            else:
                if lsx[matrix[x][y]] ==0:
                    lsx[matrix[x][y]]+=1
                elif lsx[matrix[x][y]] >=1 :
                    print ("Not Valid")
                    z=False
                    break
                if lsy[matrix[y][x]]==0:
                    lsy[matrix[y][x]]+=1
                elif lsy[matrix[y][x]] >=1 :
                    print ("Not Valid")
                    z=False
                    break
                #print (lsx,lsy)
    lsx=[0]*(n+1)
    lsy=[0]*(n+1)
if z==True:print ("Valid")