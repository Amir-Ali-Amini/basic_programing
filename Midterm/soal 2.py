n = int(input())
a = ''
for i in range(9,0,-1):
    if i <= n :
        a = str(i)+a
        n-=i
if n>0:
    print(-1)
else:
    print(a)