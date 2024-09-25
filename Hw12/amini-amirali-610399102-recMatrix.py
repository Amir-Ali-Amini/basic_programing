n=int(input())
def mtt(n):
    t=n*n-1
    return mt(t,n)
def mt(t,n):
    if t ==0 :
        return [[int(input())]]
    else :
        z=mt(t-1,n)
        if t%n==0: z.append([])
        z[-1].append(int(input()))
        return z
m = mtt(n)
for i in m :
    for j in i :
        print (j,end=' ')
    print ()
def tow(m):
    #print (m[0][0]*m[1][1]-(m[0][1]*m[1][0]))
    return m[0][0]*m[1][1]-(m[0][1]*m[1][0])
def dtr(m):
    if len (m) ==1:
        return m[0][0]
    elif len(m)==2:
        return tow(m)
    else :
        sum=0
        for i in range(len(m)):
            t=[]
            for j in range (len(m)-1):
                a=m[j+1][:i]+m[j+1][i+1:]
                t.append(a)
            #for c in a:
                #print (c)
            #print ('********')
            sum+=((-1)**i)*dtr(t)*m[0][i]
        return sum
print (dtr(m))