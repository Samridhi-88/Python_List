                           #### right ####

#n=int(input("enter any number"))
#count=0
#i=1
#while (i<=n):
#	if (n%i)==0:
#		count=count+1
#	i=i+1
#if (count==2):
#    print("prime number")
#else:
#    print("composite number")

                     #### right ####

#b=0
#while i<=100:
#    j=2
#   while j<=i//2:
#        if i%j==0:
#            count=count+1
#           break
#        j+=1
#    if count==0 and i!=1:
#        print(i,"prime")
#    else:
#        print(i,"not prime")
#    i+=1

#a=["abc","xyz","121","aba"]

                     #### wrong ####

# num=int(input("enter the num"))
# i=1
# a=[]
# while i<=num:
#     j=1
#     b=[]
#     if i==1 and j==1:
#         a.append(b)
#     else:
#         while j<=1:
#             b.append(i)
#             j+=1
#         a.append(b)
#     i+=1
# print(a)

              #### right ####

# list=["abc","xyz","121","aba"]
# i=0
# count=0
# while i<len(list):
#     j=0
#     count1=0
#     while j<len(list[i]):
#         k=-1
#         while k>=(-len(list[i])):
#             if list[i][j]==list[i][k]:
#                 count1=count1+1
#             if count1==2:
#                 count=count1
#             k-=1
#         j+=1
#     i+=1
# print(count)

                  #### wrong ####

# list=[1,2,3]
# i=0
# list1=[]
# while i<len(list):
#     l1=[]
#     l2=[]
#     l3=[]
#     if list[i]<list[1]:
#         a=(list[i],list[1])
#         l1.append(a)
#     if list[i]<list[2]:
#         b=(list[i],list[2])
#         l2.append(b)
#     if list[2]<list[2]:
#         c=list[1],list[2])
#         l3.append(c)
#     i+=1
#     list1.append(l1,l2,l3)
# print(list1)

            #### right ####

# num=int(input("enter a no="))
# i=1
# a=[]
# while i<=num:
# 	j=1
# 	b=[]
# 	while j<=10:
# 		x=i*j
# 		b.append(x)
# 		j=j+1
# 	a.append(i)
# 	a.append(b)
# 	i=i+1
# print(a)


          #### right ####

num=int(input("enter a no="))
i=1
a=[ ]
while i<=num:
	j=1
	b=[ ]
	if i==1 and j==1:
		a.append(b)
	else:
		while j<=i:
			b.append(j)
			j=j+1
		a.append(b)
	i=i+1
print(a)

        
        







    






