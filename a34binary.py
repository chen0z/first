f=int(input())
a=[1]
n=0
k=2**n
#def foundbinary(n,k) :
while f >= k :
    n=n+1
    k=2**n
else :
    n=n-1
    k=2**n
    print(n)

for i in range(0,n) :
    w=int(f%2)
    print(w)
    a.insert(1,w)
    f=f/2
print(a)
