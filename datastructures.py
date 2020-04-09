#assigning elements to different lists
Name=["Akalya","Aishu","Adi","Ashwin"]
Rollno=[3,2,1,5]
Name.sort()
Rollno.sort()
print(Name)
print(Rollno)
Name.append("Anjhanaa")
Rollno.append(4)
print(Name)
print(Rollno)
Rollno[4]=Name[4]
print(Rollno)

#accessing elements from a tuple
Name=("Akalya","Aishu","Adi","Ashwin")
Rollno=(3,2,1,5)
for i in range(len(Name)):
    print(Name[i],Rollno[i])
   
#deleting different dictionary elements
Students = {1:"Adi" , 2:"Aishu" , 3:"Akalya" , 4:"Anjhanaa"}
New={Students.pop(1)}
print(New)
print(Students)
del Students[2]
print(Students)
