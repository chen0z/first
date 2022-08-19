ID=[]
n=input()
ID=[i for i in n]
if ID[0]=='A' :
    ID.pop(0)
    ID.insert(0,'1')
    ID.insert(1,'0')
if ID[0]=='B' :
    ID.pop(0)
    ID.insert(0,'1')
    ID.insert(1,'1')
if ID[0]=='C' :
    ID.pop(0)
    ID.insert(0,'1')
    ID.insert(1,'2')
if ID[0]=='D' :
    ID.pop(0)
    ID.insert(0,'1')
    ID.insert(1,'3')
if ID[0]=='E' :
    ID.pop(0)
    ID.insert(0,'1')
    ID.insert(1,'4')
if ID[0]=='F' :
    ID.pop(0)
    ID.insert(0,'1')
    ID.insert(1,'5')
if ID[0]=='G' :
    ID.pop(0)
    ID.insert(0,'1')
    ID.insert(1,'6')
if ID[0]=='T' :
    ID.pop(0)
    ID.insert(0,'2')
    ID.insert(1,'7')
if ID[0]=='S' :
    ID.pop(0)
    ID.insert(0,'2')
    ID.insert(1,'6')

ID=list(map(eval,ID))
sumID=ID[0]+ID[1]*9+ID[2]*8+ID[3]*7+ID[4]*6+ID[5]*5+ID[6]*4+ID[7]*3+ID[8]*2+ID[9]+ID[10]

if sumID%10==0 :
    print('real')
else :
    print('fake')
