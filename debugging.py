marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0
while total_marks < len(marks):
    total_marks = total_marks + 1
    counter = counter + 1 
print(total_marks)
print(counter)


marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
i=0
total_marks =(0)
counter = 0
while i< len(marks):
    #counter = counter + 1
    total_marks=total_marks+int(marks[i])
    counter+=1
    i+=1
print(total_marks)
print(counter)
    
