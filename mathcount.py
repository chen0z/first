function=input().split()
print(function)
lista=[]
n=len(function)
z=int((n-1)/2)
k=[]
for i in range(0,z) :
    if '*' or '/' in function :
        if '*' in function :
            a=function.index('*')
        else :
            a=100
        if '/' in function :
            b=function.index('/')
        else :
            b=100
    if '+' or '-' in function :
        if '+' in function :
            c=function.index('+')
        else :
            c=100
        if '-' in function :
            d=function.index('-')
        else :
            d=100
#print(a,b,c,d)

    #if a or b !=0 :
        if a < b :
            l=a-1
            s=int(function[l])
            k.append(s)
            l=a+1
            s=int(function[l])
            k.append(s)
            ans=k[0]*k[1]
            k.clear()
            function.pop(a)
            function.pop(a)     #is f[a+1]
            function.pop(a-1)
            function.insert(a-1,ans)
        #is putin f[a]
        elif b!=100 :
            l=b-1
            s=int(function[l])
            k.append(s)
            l=b+1
            s=int(function[l])
            k.append(s)
            ans=int(k[0]/k[1])
            k.clear()
            function.pop(b)
            function.pop(b)     #is f[a+1]
            function.pop(b-1)
            function.insert(b-1,ans)
    #else :
        if c < d :
            l=c-1
            s=int(function[l])
            k.append(s)
            l=c+1
            s=int(function[l])
            k.append(s)
            ans=k[0]+k[1]
            k.clear()
            function.pop(c)
            function.pop(c)     #is f[a+1]
            function.pop(c-1)
            function.insert(c-1,ans)
        #is putin f[a]
        elif d!=100 :
            l=d-1
            s=int(function[l])
            k.append(s)
            l=d+1
            s=int(function[l])
            k.append(s)
            ans=k[0]-k[1]
            k.clear()
            function.pop(d)
            function.pop(d)     #is f[a+1]
            function.pop(d-1)
            function.insert(d-1,ans)
    print(function)
