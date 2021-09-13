List=[[1,5,6],2,3,[5,9],3]
Sum=0
S=0
i=0
while i<len(List):
    if type(List[i]) is list:
        j=0
        while j<len(List[i]):
            Sum+=List[i][j]
            j+=1
    else:
        S+=List[i]
    i+=1
Total_Sum=S+Sum
print(Total_Sum)