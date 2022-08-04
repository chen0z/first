f=list(input().split())
#mul_time=f
n=len(f)
ans=0
k=[]
a=[]
b=[]
c=[]
d=[]
print(f)
#print(n)
for i in range(0,n) :
    a.append(f.index('+',i))
    #c=f.index('*')
    #d=f.index('/')
    if f[i]=='*' or f[i]=='/' : 
        l=i-1
        s=int(f[l])
        k.append(s)
        l=i+1
        s=int(f[l])
        k.append(s)
        if f[i]=='*' :
            ans=k[0]*k[1]
        elif f[i]=='/' : 
            ans=k[0]/k[1]
        k.clear()
        
    if f[i]=='+' or f[i]=='-' :
        l=i-1
        s=int(f[l])
        k.append(s)
        l=i+1
        s=int(f[l])
        k.append(s)
        if f[i]=='+' :
            ans=k[0]+k[1]
        elif f[i]=='-' :
            ans=k[0]-k[1]
        k.clear()
        
print(ans)
print(a)   
