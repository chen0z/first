s=list(map(int,input().split()))
a=[]
p=0
m=0
k=0
n=s[0]-1
a.insert(0,s[1])
for q in range (0,s[0]):
    a.append(0)

for i in range (2,s[0]+1) :
    for j in  range (0,s[0]) :
        if s[i]>a[j] :
            k=j
            break
            #a.insert(j,s[i])
        else :
            m=m+1
    a.insert(k,s[i])
    if m==s[0] :
        a.insert(a[n],s[i])
        m=0

for q in range(0,s[0]):
    a.pop()

print(a)

for x in range (1,s[0]):
    if a[x]+1==a[x-1] :
        p=p+1
    else :
        print('NO')
        break

if p==n :
    print('YES')
