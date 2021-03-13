num=[24,33,44,5,21,19,23,30]
print("unsort list",num)
i=0
c=0
while i<len(num):
    j=0
    while j<len(num):
        if num[i]<num[j]:
            c=num[j]
            num[j]=num[i]
            num[i]=c
        j+=1
    i+=1
print("sort list",num)