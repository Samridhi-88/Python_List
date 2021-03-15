a=[[8,3,4],[1,5,9],[6,7,2]]
c=0
d=0
d1=0
diagonald=[]
while c<len(a):
    s=a[c][d]
    diagonald.append(s)
    c+=1
    d+=1
print(diagonald)

a=[[8,3,4],[1,5,9],[6,7,2]]
c=0
f=len(a)-1
d1=0
diagonal1=[]
while c<len(a):
    s=a[c][f]
    diagonal1.append(s)
    c+=1
    f+=1
print(diagonal1)