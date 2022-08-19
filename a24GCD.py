#為何while a>=b 沒辦法自己跳出迴圈呢
a,b=map(int,input().split())

if a<b :
    c=a
    a=b
    b=c     #a大b小
print(a,b)
while a!=0:
    while a>=b : 
        a=a-b
        print('n=',a,'b=',b)
        if a<b :
            print('e')
            break
    else :
        c=a 
        a=b
        b=c
        print('d')
else :
    print(b)
