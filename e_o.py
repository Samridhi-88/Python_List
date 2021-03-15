list=[90,80,3,5,13,55,74]
i=0
e_s=0
o_s=0
while i<len(list):
    if list[i]%2==0:
        e_s+=list[i]
    else:
        o_s+=list[i]
    i=i+1
print(e_s)
print(o_s)