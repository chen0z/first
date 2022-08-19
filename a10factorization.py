n=int(input())
#質數2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
float(n)
a=0
b=0 
c=0
d=0
while n%2==0 :
    a=a+1
    n=n/2
print('a=',a)
while n%3==0 :
    b=b+1
    n=n/3
print('b=',b)
while n%5==0 :
    c=c+1
    n=n/5
print('c=',c)
while n%7==0 :
    d=d+1
    n=n/7
print('d=',d)
if a==0 and b==0 and c==0 and d == 0 :    
    print(n)
else :
    if a!=0 :
        print('2 ^',a, end ='')
    if b!=0 :
        print('*3 ^',b,end='')
    if c!=0 :
        print('*5 ^',c,end='')
    if d!=0 :
        print('*7 ^',d,end='')
    
