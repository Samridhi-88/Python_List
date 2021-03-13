chr=["a","n","t","a","a","t",'n',"n","a","x","u","g","a","a","x","a"]
a=[]
i=0
while i<len(chr):
    j=0
    b=[]
    counter=0
    while j<len(chr):
        if chr[i]==chr[j]:
            counter+=1
        j+=1
    b.append(chr[i])
    b.append(counter)
    if b not in a:
        a.append(b)
    i+=1
print(a)

