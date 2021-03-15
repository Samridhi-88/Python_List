num=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(num):
    if num[i]>max:
        max=num[i]
    i=i+1
print(max)




num=int(input("enter the num"))
num1=int(input("enter the num"))
num2=int(input("enter the num"))
a=[]
a.append(num)
a.append(num1)
a.append(num2)
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
print(max)