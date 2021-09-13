list=[1,2,3]
i=0
new=[]
while i<len(list):
    List1=[]
    List2=[]
    List3=[]
    if list[i]<list[1]:
        first=list[i]
        first1=list[1]
        List1.append(first)
        List1.append(first1)
    if list[i]<list[2]:
        second=list[i]
        second1=list[2]
        List2.append(second)
        List2.append(second1)
    if list[1]<list[2]:
        third=list[1]
        third1=list[2]
        List3.append(third)
        List3.append(third1)
    new.append(List1)
    new.append(List2)
    new.append(List3)
    i+=1
    if List1 and List2 and List3 in new:
        break
print(new)
