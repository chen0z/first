n=[]
a=input()
n=[i for i in a]
u=[]
l=len(n)

for j in range(0,l) :
    k=n[l-j-1]
    u.append(k)
#print(u)
if u==n :
    print('yes')
else :
    print('no')
